Based on [the doggie book](https://learning.oreilly.com/library/view/flask-web-development/9781491991725/)

### Demo

[demo](http://120.78.214.127)

### Dependencies

python3

pipenv

flask

flask-bootstrap

... and lots of tool, I'll put there late

### Install

Install pipenv at first,
create a virtual environment

    pipenv install
    pipenv shell
    flask run




### Todo
<s>comments</s>

<s>follower&following lists</s>

all the test case

a better email html page


-----------------All texts below is my nonsense-------

pipenv shell & exit

each time change .env

need to exit virtualenv and reinitiate again

pipenv install python-dotenv

---------------------------------------------------
deployed with docker


----------------------------------------------------
### Create database tables

```
flask shell
>>>from app.models import db
>>>db.drop_all() 
>>>db.create_all()
```

drop old tables and create new

### Insert Rows

```
>>>from app import User,Role
>>>admin_role = Role(name='Admin')
>>>user_susan = Role(username='susan',role=user_role or admin_role etc)
>>>db.session.add(admin_role) or add_all([admin_role,user_susan])
>>>db.session.commit()
```

### Modify & delete & query Rows

```
>>>admin_role.name ='Administrator' & session.add & commit
>>>db.session.delete(rolename) & commit
>>>Role.query.all() || filtry_by(role=).all()
```

-------------------------------------------------------------

### Migrate

```
sudo pipenv install flask-migrate
flask db init
flask db migrate -m "initial migration"
flask db upgrate
```
