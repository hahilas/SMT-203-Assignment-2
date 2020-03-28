import datetime

from app import db

class User(db.Model):
	__tablename__ = 'user'

	# start your code after this line
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	contact_number = db.Column(db.Integer, unique=True, nullable=False)
	
	#one-to-many model
	temperatures = db.relationship('Temperature', back_populates='user', uselist= True, cascade='all,delete-orphan', lazy=True)
	# end your code before this line

	def __init__(self, name, contact_number,temperatures=None):
		# start your code after this line
		self.name = name
		self.contact_number = contact_number
		self.temperatures = [] if temperatures is None else reviews
		# end your code before this line

	def __repr__(self):
		return '{} was created with id {}'.format(self.name, self.id) 
		
	def serialize(self):
		# start your code after this line
		return {
			'name': self.name, 
			'id':self.id,
			'contact_number': self.contact_number,
		}
		# end your code before this line

class Temperature(db.Model):
	__tablename__ = 'temperature'

	# start your code after this line
	id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
	temp_value = db.Column(db.Float, unique=False, nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	#one-to-many model
	user = db.relationship('User', back_populates='temperatures')
	# end your code before this line

	def __init__(self, temp_value, user_id):
		# start your code after this line
		self.temp_value = temp_value
		self.user_id = user_id
		# end your code before this line

	def __repr__(self):
		return '{}'.format(self.temp_value) 
		
	def serialize(self):
		# start your code after this line
		return {
			'user_id': self.user_id, 
			'temp_value': self.temp_value,
			'timestamp': self.timestamp,
		}
		# end your code before this line