from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file('index.html')

@app.route("/api/hakk", methods=["POST"])
def receive_hakk():
    print(request.form)
    return "Success!"

def formatInput(string):
	comma = ","
	junk = re.findall(r"[\w']+", string)
	result = []
	for item in junk:
		if item.isalpha():
			result.append(item)
	comma = comma.join(result)
	return comma


if __name__ == "__main__":
    app.run()