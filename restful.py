from flask import Flask,jsonify,request,session,render_template,g
import numpy as np
app = Flask(__name__)
app.config['SECRET_KEY']='Mysecret!'
languages=[{'name':'c'},{'name':'c++'},{'name':'python'}]
@app.route('/',methods=['GET'])
def default():
    return jsonify({'message':'welcome'})

@app.route('/lang',methods=['GET'])
def langall():
    return jsonify({'languages':languages})
@app.route('/lang/<string:name>',methods=['GET'])
def langone(name):
        lang=[language for language in languages if language['name']==name]
        return jsonify({'languages':lang[0]})

@app.route('/updatelang',methods=['POST'])
def updatelang():
    lang={'name':request.json['name']}
    languages.append(lang)
    print(languages)
    return jsonify({'message':'your data is posted succesfully.'})
@app.route('/updatelang/<string:name>', methods=['PUT'])
def editOne(name):
	lang=[language for language in languages if language['name']==name]
	lang[0]['name']= request.json['name']
	return jsonify({'language':lang[0]})
@app.route('/temp',methods=['POST'])
def get_tempreture():
    temp=request.json['temp']
    print(temp)
    return jsonify({'message':"i got temp"})
if __name__ == '__main__':
    app.run(debug=True)
