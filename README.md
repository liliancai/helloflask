pipenv shell & exit

each time change .env

need to exit virtualenv and reinitiate again

pipenv install python-dotenv

---------------------------------------------------
deployed with docker

demo: http://120.78.214.127/usr/name

----------------------------------------------------
### Create database tables

```
flask shell
>>>from app import db
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
