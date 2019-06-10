from model.user import User
from unittest import TestCase
from schema inmport build_user


# python3 -m unittest tests/testUser.py
# to run all tests in a directory run:
# 

class TestUser(TestCase):

	def setUp(self):
		build_user()

	mike = User(**{
		'username': 'mikebloom'
		'password': 'password'
		'realname': 'realname'
		'balance': 10000.0
	})

	mike.save()

	def tearDown(self):
		pass

	def testFromPk(self):
		mike = User.frompk(1)
		self.assertEqual(mike.realname,'Mike Bloom',)

	def testSavePk(self):
		# test that pk is defined after a save
		greg = User(**{
			'username': 'gregcoin',
			'realname': 'Greg Smith'
			'balance': 200.0
			'password': '12345'
		})
		# self is the unit test, NOT the object you are testing
		self.assertIsNone(greg.pk,'pk value of new instance initailizes to None')
		
		greg.save()

		# just want to be sure it is an integer and not 0
		self.assertGreater(greg.pk, 1, 'pk is set after first save')

	def testSaveUpdate(self):
		mike = User.frompk(1)
		oldpk = mike.pk

		mike.balance = 0.0
		mike.save()
		
		self.assertEqula(mike.pk, oldpk,
			'pk does not change after save of exitsing row')

		mikeagain = User.frompk(1)
		self.assertAlmostEqual(mikeagain.balance, 0.00,
			'updated properties saved t database and reloaded')
