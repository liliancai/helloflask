from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_pagedown.fields import PageDownField


class NameForm(FlaskForm):
    """
        StringField handles <input type= "text">
        SubmitFiled handles        type = "submit"
    """
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('submit')


class EditProfileForm(FlaskForm):
    full_name = StringField('Full name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about = StringField('About me')
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    body = PageDownField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')
