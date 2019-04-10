import unittest
from app.models import User, Permission, AnonymousUser


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password = 'gizmo')
        self.assertTrue(u.password_hash is not None)

    def test_password_getter(self):
        u = User(password = 'gizmo')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password = 'gizmo')
        self.assertTrue(u.verify_password('gizmo'))
        self.assertFalse(u.verify_password('kitty'))

    def test_password_salts_are_random(self):
        u = User(password = 'gizmo')
        u2 = User(password = 'kitty')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_user_role(self):
        u = User(email='test@test.com', password='test')
        self.assertTrue(u.can(Permission.FOLLOW))
        self.assertTrue(u.can(Permission.COMMENT))
        self.assertFalse(u.can(Permission.MODERATE))

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.FOLLOW))
        self.assertFalse(u.can(Permission.COMMENT))
