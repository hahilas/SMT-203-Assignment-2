# Step 01: import necessary libraries/modules
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# your code begins here 

# Step 02: initialize flask app here 
app = Flask(__name__)
app.debug = True

# Step 03: add database configurations here
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://asm02_user:password@localhost:5432/asm02'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Step 04: import models
from models import User, Temperature

# Step 05: add routes and their binded functions here
@app.route('/user/', methods=['POST']) 
def create_user():
	print('create_user')

	# start your code after this line
	# get values from request.json 
	name = request.json['name'] 
	contact_number = request.json['contact'] 

	try:
		new_user = User(name=name, contact_number=contact_number)
		db.session.add(new_user)
		db.session.commit() # this must be done before adding reviews
		if len(str(contact_number))==8:
			return jsonify('new user {}'.format(new_user))
		else:
			return "Please type an 8 digit number" 
		

	except Exception as e:
		return (str(e))
	# end your code before this line

@app.route('/temp/', methods=['POST']) 
def create_temp():
	print('create_temp')

	# start your code after this line
	if 'name' and 'temp' in request.json:
		name = request.json['name']
		temp_value = request.json['temp']
	else:
		return "Please ensure you have written the field names correctly"
	
	if isinstance(name,str)==False or isinstance(temp_value,float)==False :
		return "Please make sure your input data types are correct. Check if your name is in string and temp is in float."
	
	if name=="":
		return "Please ensure your friend's name is filled up."

	check_name = User.query.filter_by(name=name).first()

	if check_name is None:
		return jsonify('user {} does not exist'.format(name))
	
	
	try: #select user_id  where name = name
		user_id = db.session.query(User.id).filter(User.name==name)
		# User.query(User.id).filter(User.name == name).first()
		if user_id != None:
			new_temp = Temperature(user_id=user_id, temp_value=temp)
			db.session.add(new_temp)
			db.session.commit()
			return jsonify('new temp record {} was created for user {}'.format(new_temp,name))
		else:
			return "Are you sure {} is your friend?".format(name)


		# this must be done before adding reviews
	except Exception as e:
		return (str(e))

# 	# end your code before this line

# @app.route('/friend/', methods=['PUT']) 
# def update_friend():
# 	print('update_friend')

# 	# start your code after this line

# 	# end your code before this line

# @app.route('/user/', methods=['GET']) 
# def get_user():
# 	print('get_user')

# 	# start your code after this line

# 	# end your code before this line

# @app.route('/temp/', methods=['GET']) 
# def get_temp():
# 	print('get_temp')

# 	# start your code after this line

# 	# end your code before this line

# # your code ends here 

if __name__ == '__main__':
	app.run(debug=True)