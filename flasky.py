import os
from app import create_app, db
# print(test)
from app.models import User, Role
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
print(os.environ.get('FLASK_APP'))
print("Hi am flasky")
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
	return dict(db=db, User=User, Role=Role)

@app.cli.command()
def test():
	"""Run to tests."""
	import unittest
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)
