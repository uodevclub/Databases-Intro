#!flask/bin/python
from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def index():
	return "Connected"

@app.route('/person/<username>',methods=['GET'])
def get_person(username):
	pass

@app.route('/topic/<topic>',methods=['GET'])
def get_topic(topic):
	pass

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__=='__main__':
	app.run(debug=True)
