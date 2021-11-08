#importing flask
from flask import Flask,jsonify,request
app=Flask(__name__)   #---defining app using flask

@app.route('/',methods=['GET'])
def hello():
    return 'helloworld'
#giving details of customer list
details=[{'name':'sridevi',
          'mail':'sridevibilla@gmail.com',
          'phone':7035216581
          },
          {'name':'sai',
           'mail':'sai12@gmail.com',
           'phone':8502315656
          },
          {
            'name':'hari',
            'mail':'hari21@gmail.com',
            'phone':9440866586
          }
]
@app.route('/details',methods=['GET'])
def user():
    return jsonify({'details':details})

if __name__=="__main__":
    app.run(debug=True)  #===runing the appdetails

