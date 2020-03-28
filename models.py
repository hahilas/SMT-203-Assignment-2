import datetime
from app import db

# user_temp_table = db.Table('user_temp', 
# 	db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
# 	db.Column('temperature_id', db.Integer, db.ForeignKey('temperature.id'), primary_key=True)
# )

class User (db.Model):
	__tablename__ = 'user'

	# start your code after this line
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	contact_number = db.Column(db.Integer, unique=True, nullable=False)

	#one-to-many model
	temperatures = db.relationship('Temperature', back_populates='users', uselist=True)
	# end your code before this line

	def __init__(self, name, contact_number, temperatures=None):
		# start your code after this line
		self.name = name
		self.contact_number = contact_number
		# self.temperatures = temperatures
		# self.temperatures = [] if temperatures.temp_value is None else temperatures.temp_value
		# end your code before this line

	def __repr__(self):
		return '<name {} id {} and contact number {} >'.format(self.name, self.id, self.contact_number) 

	def serialize(self):
		# start your code after this line
		return {
			'contact_number': self.contact_number,
			'name': self.name, 
			'id':self.id,
			# 'temp_logs': self.temperatures
			# [t.temp_value for t in self.temperatures] 
			# 'temp_logs': [t.temp for t in self.temp_logs]
		}
		# end your code before this line

class Temperature(db.Model):
	__tablename__ = 'temperature'

	# start your code after this line
	id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
	temp_value = db.Column(db.Float, unique=False, nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
	# user_name = db.Column(db.String(80), db.ForeignKey('user.name'), nullable=False)
	# user = db.Column(db.Integer, db.ForeignKey('user.id','user.name'), nullable=False)
	# user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	
	#one-to-many model
	users = db.relationship('User', back_populates='temperatures')
	# user_name = db.Column(db.String(80), db.ForeignKey('user.name'), nullable=True)
	
	#many-to-many model
	# users = db.relationship('User', secondary=user_temp_table, back_populates='temperatures')
	# end your code before this line

	def __init__(self, temp_value, user_id, ):
		# start your code after this line
		self.temp_value = temp_value
		self.user_id = user_id
		# self.user_name = user_name
		# end your code before this line

	def serialize(self):
		# start your code after this line
		return {
			'id': self.id,
			'temp_value': self.temp_value,
			'timestamp': self.timestamp,
			'user_id': self.user_id, 
			'user_name': self.user_name

		}
		# end your code before this line
