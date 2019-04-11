Based on [the doggie book](https://learning.oreilly.com/library/view/flask-web-development/9781491991725/)

### Dependencies

pipenv
flask
flask-bootstrap
flask-sqlach"#¤!"#¤(I never remember the name...)
... and lots of tool, I'll put there later...

### Todo
comments
follower&following lists
all the test cases

-----------------All texts below is my nonsense-------
pipenv shell & exit

each time change .env

need to exit virtualenv and reinitiate again

pipenv install python-dotenv

---------------------------------------------------
deployed with docker

[demo](http://120.78.214.127)

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
