from flask import Flask , jsonify , request

app = Flask(__name__)
contacts = [
    {'id': 1, 
    'name': u'roopesh',
    'contact': u'9080706050',
    'status': False},
    {'id': 2, 
    'name': u'modi',
    'contact': u'1234567890',
    'status': False}
]


@app.route("/")
def print():
    return "HELLO"

@app.route("/get-contact")
def get_task():
    return jsonify({ 
        "data":contacts
    })

@app.route("/add-contact", methods = ["POST"])
def add_task():
    if not request.json :
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)
    info = {
        'id':contacts[-1]['id']+1 ,
        'name':request.json['name'],
        'contact':request.json['contact'],
        'status':False
    }
    contacts.append(info)
    return jsonify({
        'status':"sucess",
        'message':"Task added sucessfully"
    })

if __name__ == "__main__":
    app.run(debug=True)
