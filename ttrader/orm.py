import sqlite3

class Sqlite3ORM:
	fields = []
	dpath = ''
	dtable =''
	create = ''

def __init__(self):
	raise NotImplementedError

	@classmethod
	def_create_insert(cls)
		columnlist = ', '.join(cls.fields)
		qmarks = ', '.join("?" for val in cls.fields)
		SQL = '''INSERT INTO {tablename} ({columnlist})
		VALUES ({qmarks})'''
		return SQL.format(tablename=cls.dbtable,columnlist=columnlist,qmarks=qmarks)

	def save(self):
		if self.pk is None:
			self._insert()
		else:
			self._update()


	def _insert(self):
		with sqlite3.connect(self.dbpath) as conn:
			cur = conn.cursor()
			SQL = self._create_insert()
			propvals = [getattr(self, propname) for propname in self.fields]
			cur.execute(SQL,propvals)
			self.pk = cur.lastrowid

	@classmethod
	def _create_update(cls):
		# returna  generic UDPATE SQL command like create insert
		# update pk WHERE pk = ?

	def _update(self):
		# 
		# will also have to provide self.pk for that ? in 
		# adition to the field values	
