from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    result = request.json["number"] + 1

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(port="8080")

