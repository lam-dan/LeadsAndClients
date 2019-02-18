from flask import Flask, render_template, request, session, redirect

# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
import copy
app = Flask(__name__)
app.secret_key = "ThisIsASecret"

# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
# mysql = connectToMySQL('mydb')

# now, we may invoke the query_db method
# print("all the users", mysql.query_db("SELECT * FROM users;"))


# mysql = connectToMySQL("friendsdb")
# all_friends = mysql.query_db("SELECT * FROM friends")
# print("Fetched all friends", all_friends)

@app.route('/')

def index():

	mysql = connectToMySQL("lead_gen_business")
	all_leads = mysql.query_db("select clients.first_name, clients.last_name, count(leads.leads_id) from clients inner join sites on sites.client_id = clients.client_id inner join leads on sites.site_id = leads.site_id group by clients.client_id")
	

	dict2 = copy.deepcopy(all_leads)

	sum = 0

	for totalleads in all_leads:
		sum += totalleads['count(leads.leads_id)']
	
	print (sum)

	for person in dict2:
		person['count(leads.leads_id)'] = str(round(person['count(leads.leads_id)']/sum * 100,2))

	print (dict2)

	# dict2 = copy.deepcopy(dict1)
	# for loop to find the total using the first dictionary
	# use the second dictionary to update its own values to be
	# values of itself / the sum you get from the for loop.

	# print("leads", all_leads)

	return render_template('leads_and_clients.html',leads = all_leads, percent = dict2)
	# , percent = dict2)
# friends = all_friends

# @app.route('/add', methods=['POST'])

# def create():
# 	mysql = connectToMySQL("lead_gen_business")
# 	query = "INSERT INTO leads (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
	


# 	data = {
# 	         'first_name': request.form['first_name'],
# 	         'last_name':  request.form['last_name'],
# 	         'occupation': request.form['occupation']
# 	       }

# 	new_friend_id = mysql.query_db(query, data)

# 	print (query)

# 	return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)
