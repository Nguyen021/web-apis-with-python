from flask import jsonify, request

from main import myapp


# http://127.0.0.1:5000/?name=nguyen
@myapp.get("/")
def index():
    name = request.args.get("name")
    if not name:
        return jsonify({"status": "error can't find name"})
    res = {"data": f"Xin chào , {name} !"}
    return jsonify(res)


# Multi-argument interactive API
# http://127.0.0.1:5000/hello?first_name=nguyen
@myapp.get("/hello")
def hello():
    first_name = request.args.get("first_name", default="This is first_name default")
    last_name = request.args.get("last_name", default="This is last_name default")
    response = {"data": f"Is your name - {first_name} - {last_name} ?"}
    return jsonify(response)
