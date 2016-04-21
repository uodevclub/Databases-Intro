from flask import Flask, jsonify, request
from TwitterAPI import TwitterAPI
import psycopg2
import sys
from CONFIG import *
app = Flask(__name__)

twitter_api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

db_connect = None
try:
	#Create your database
	db_connect = psycopg2.connect(database=database_name,user=database_user,password=database_password)

	# Create client cursor to execute commands
	cursor = db_connect.cursor()
	cursor.execute("CREATE TABLE Users (id SERIAL PRIMARY KEY, name VARCHAR, username VARCHAR,followers_count INTEGER);")
	#The variables placeholder must always be a %s, psycop2 will automatically convert the values to SQL literal

	###EXECUTE TEST COMMAND HERE###
	db_connect.commit()

	cursor.execute("SELECT * FROM Users")

	print(cursor.fetchone())

except psycopg2.DatabaseError as e:

	print ('Error %s' % e)

	sys.exit(1)

finally:
	if db_connect:
		db_connect.close()


@app.route('/person', methods=['GET'])
def get_person():
	"""
		Get person by searching for a twitter handle
		URL parameters:
			q : search query string
	"""
	query = request.args.get('q')
	if query is None:
		return "No query found"

	result = twitter_api.request('users/show', {'screen_name' : query})
	person = result.json()
	return jsonify({
		'screen_name': person['screen_name'],
		'name': person['name'],
		'followers_count': person['followers_count']
	})

@app.route('/topic', methods=['GET'])
def get_topic():
	"""
		Get topic by searching
		URL parameters:
			q : search query string
	"""
	query = request.args.get('q')
	if query is None:
		return "No query found"

	result = twitter_api.request('search/tweets', {'q' : query})
	statuses = result.json()['statuses']
	tweets = []
	for status in statuses:
		tweets.append(status['text'])

	return jsonify({"tweets": tweets})

if __name__=='__main__':
	app.run(debug=True)
