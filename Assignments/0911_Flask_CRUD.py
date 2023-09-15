from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price": 3800},
    {"id":2, "name":"Americano", "price": 4300},
    {"id":3, "name":"Caffe Latte", "price": 5000},
]
@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /menus | 자료를 가지고 온다
@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})

# POST /menus | 자료를 자원에 추가한다
@app.route('/menus', methods = ['POST'])
def create_menu():
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()
    new_menu = {
        "id": 4,
        "name": request_data['name'],
        "price": request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)


## mandatory
# PUT
@app.route('/menus/<int:id>', methods = ['PUT'])
def update_menu(id):
    for x in menus:
        if x['id'] == id:
            request_data = request.get_json()
            x["name"] = request_data['name']
            x["price"] = request_data['price']
            return jsonify(menus)

# DELETE
@app.route('/menus/<int:id>', methods = ['DELETE'])
def delete_menu(id): 
    for x in menus:
        if x['id'] == id:
            menus.remove(x)
            return jsonify(menus)


## bonus 1
@app.route('/menus', methods = ['POST'])
def create_menu(): 
    request_data = request.get_json()
    new_menu = {
        "id": len(menus)+1,
        "name": request_data['name'],
        "price": request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)


if __name__ == '__main__':
    app.run()
