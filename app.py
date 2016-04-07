from flask import Flask, jsonify, request
from TwitterAPI import TwitterAPI

app = Flask(__name__)
twitter_api = TwitterAPI('TvgYpf2f9KDReUxp8MrjWQ5QZ', 'NbfflAQu3N1S7S7VGqXhonVjGM0qbiMcaJtqpoJEno6eb3hHko', '364104026-GxEOLphvkmGrOhQuuWnudDdVydmCkcgQwy2zpkfQ', '0bBBcrmO7IuyKa4q83UtodNn8xWUyGT3WCJ9zIyOM4wIW')

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
