from flask import Flask, request, jsonify
from flask_cors import CORS
from SinglyLinkedList import LinkedList

app = Flask(__name__)
CORS(app=app)

favorite_list = LinkedList()


@app.route("/favorites/<fox_id>", methods=["POST"])
def favorites(fox_id):
    favorite_list.add_first(fox_id)
    return jsonify({"Status": "OK", "FOXs": fox_id})


@app.route("/my_favorites")
def my_favorites():
    print(favorite_list.linked_list_to_list())
    response = {"data": favorite_list.linked_list_to_list()}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
