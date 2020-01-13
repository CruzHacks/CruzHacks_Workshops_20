from flask import Flask, jsonify, request
import json

app = Flask(__name__)

hackers_data = []


@app.route("/", methods=["GET"])
def home():
    """ This functions returns the data for an argued hacker.
        If no "index" argument is given in the query
        parameter than all the hackers are returned.
    """

    target_index = request.args.get("index")

    with open('hackers.json', 'r') as json_file:
        hackers_data = json.load(json_file)

        if target_index is not None:
            hackers_data = [
                hacker for hacker in hackers_data
                if hacker["index"] == int(target_index)
            ]

    return jsonify(hackers_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)