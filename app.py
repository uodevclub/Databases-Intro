from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/person/<username>',methods=['GET'])
def get_person(username):
	pass

@app.route('/topic/<topic>',methods=['GET'])
def get_topic(topic):
	pass

if __name__=='__main__':
	app.run(debug=True)
