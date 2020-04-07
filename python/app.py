from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    option_receive = request.form['option_give']
    address_receive = request.form['address_give']
    phonenumber_receive = request.form['phonenumber_give']

    order = {
        'name': name_receive,
        'option': option_receive,
        'address': address_receive,
        'phone': phonenumber_receive
    }

    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 접수되었습니다.'})


@app.route('/order', methods=['GET'])
def read_orders():
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
