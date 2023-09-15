from flask import Flask, jsonify, request

app = Flask(__name__)

weapons = []

@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /whoami
@app.route('/whoami')
def get_id():
    return jsonify({"name": "chae-youn"})

# GET /echo?string="string"
@app.route('/echo')
def echo_string():
    query_string = request.args.get('string')
    return jsonify({"value": query_string})

# POST /weapon
@app.route('/weapon', methods = ['POST'])
def create_weapon():
    request_data = request.get_json()
    new_weapon = {
        'name' : request_data['name'],
        'stock' : request_data['stock']
    }
    weapons.append(new_weapon)
    return jsonify(new_weapon)

# GET /weapon
@app.route('/weapon')
def get_weapon():
    return jsonify(weapons)

# PUT /weapon/<string:name>
@app.route('/weapon/<string:name>', methods = ['PUT'])
def update_weapon(name):
    for x in weapons:
        try:
            if x["name"] == name:
                request_data = request.get_json()
                x["name"] = request_data['name']
                x["stock"] = request_data['stock']
                return jsonify(weapons)
        except KeyError:
            return jsonify({"error": "Invalid JSON data"})

# DELETE /weapon/<string:name>
@app.route('/weapon/<string:name>', methods = ['DELETE'])
def delete_weapon(name): 
    try:
        for x in weapons:
            if x['name'] == name:
                weapons.remove(x)
                return jsonify(weapons)
    except KeyError:
        return jsonify({"error": "Invalid JSON data"})
        
if __name__ == '__main__':
    app.run()
