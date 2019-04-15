from . import main
from .. import db
from flask import render_template, flash, request, redirect, url_for,\
    current_app, abort, make_response
from flask_login import login_required, current_user
from ..models import User, Post, Permission, Comment
from .forms import EditProfileForm, PostForm, CommentForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE) and form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    show_followed = False
    if current_user.is_authenticated:
        show_followed = bool(request.cookies.get('show_followed', ''))
    if show_followed:
        query = current_user.followed_posts
    else:
        query = Post.query
    pagination = query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    posts = pagination.items
    return render_template('index.html', form=form, posts=posts,
                           Permission=Permission, show_followed=show_followed,
                           pagination=pagination)
    # Miguel's code don't pass permission, tried use {{super()}}, not work


@main.route('/usr/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    posts = pagination.items
    return render_template('user.html', user=user, posts=posts,
                           pagination=pagination, Permission=Permission)


@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.full_name = form.full_name.data
        current_user.location = form.location.data
        current_user.about_me = form.about.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash("You've updated your profile")
        return redirect(url_for('.user', username=current_user.username))
    form.full_name.data = current_user.full_name
    form.location.data = current_user.location
    form.about.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data,
                          post=post,
                          author=current_user._get_current_object())
        db.session.add(comment)
        db.session.commit()
        flash('Your just left a commnet')
        return redirect(url_for('.post', id=post.id, page=1))
    page = request.args.get('page', 1, type=int)
    if page == -1:
        page = (post.comments.count() - 1) // \
               current_app.config['FLASKY_COMMENTS_PER_PAGE'] + 1
    pagination = post.comments.order_by(Comment.timestamp.asc()).paginate(
                 page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'],
                 error_out=False)
    comments = pagination.items
    return render_template('post.html', posts=[post], form=form,
                           comments=comments, pagination=pagination)


@main.route('/edit_post/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Post.query.get_or_404(id)
    if post.author != current_user and\
       not current_user.is_adminstrator():
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.body = form.body.data
        db.session.add(post)
        db.session.commit()
        flash("You just edited this post")
        return redirect(url_for('.index'))
    form.body.data = post.body
    return render_template('edit_post.html', post=post, form=form)


@main.route('/delete_post/<int:id>', methods=['GET'])
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    if post.author != current_user and not current_user.is_adminstrator():
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("You deleted a post")
    return redirect(url_for('.index'))


@main.route('/follow/<username>')
@login_required
# @permission_required(Permission.FOLLOW)
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User not exist')
        return redirect(url_for('.index'))
    current_user.follow(user)
    db.session.commit()
    flash('You have followed %s' % username)
    return redirect(url_for('.user', username=username))


@main.route('/unfollow/<username>')
@login_required
# @permission_required(Permission.FOLLOW)
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None or not current_user.is_following(user):
        flash('User not exist or unfollowed areadly')
        return redirect(url_for('.index'))
    current_user.unfollow(user)
    db.session.commit()
    flash('You have unfollowed %s' % username)
    return redirect(url_for('.user', username=username))


@main.route('/all')
@login_required
def show_all():
    resp = make_response(redirect(url_for('.index')))
    resp.set_cookie('show_followed', '', max_age=30*24*60*60)
    return resp


@main.route('/followed')
@login_required
def show_followed():
    resp = make_response(redirect(url_for('.index')))
    resp.set_cookie('show_followed', '1', max_age=30*24*60*60)
    return resp
