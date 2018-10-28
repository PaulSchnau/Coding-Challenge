from flask import Flask, request, jsonify
from hashlib import sha256
app = Flask(__name__)

messages = {
	# sha256digest: the_message
}

@app.route('/messages', methods=['POST'])
def post_message():
	message = request.json.get('message', None)
	if message is not None:
		digest = sha256(message.encode('utf-8')).hexdigest()
		messages[digest] = message
		return jsonify({"digest": digest})
	else:
		return {"err_msg": "No message in posted JSON"}

@app.route('/messages/<digest>', methods=['GET'])
def get_message(digest):
	if digest in messages:
		return jsonify({"message": messages[digest]})
	else:
		return jsonify({"err_msg": "Message not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
