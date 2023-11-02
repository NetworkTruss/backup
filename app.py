from flask import *
from flask import request, redirect
from flask import render_template
from algo import mlalgo
from flask import Flask, jsonify, make_response
import pymysql
app = Flask(__name__)

try:
    connection=pymysql.connect(host="truss.clwk1t6znrss.ap-south-1.rds.amazonaws.com",user='admin',password='axtrixninjastar321',db='truss', autocommit=True)
    cursor=connection.cursor()
except Exception as e:
    print("database conn failed")

application = app
app.debug = True

# Sign In Page
@app.route('/')
def home():
	return render_template('index.html')
	
#done with upload
data_res = []

@app.route('/data', methods = ['POST', 'GET'])
def upload():
    data = request.data
    print(data)
    session = "aayushisarda1378@gmail.com"
    data=mlalgo(session)
    users=data.to_dict(orient='records')
    users = [d for d in users if d.get('email') != session]
    ans = cursor.execute(f"select * from truss_data where email!='{session}' LIMIT 20")
    data2 = cursor.fetchall()
    data_res = [list(inner_tuple) for inner_tuple in data2]
    response_data = {
          "users" : users,
          "data2" : data_res,
          "ans" : ans
    }
    return jsonify(response_data)


if __name__ == '__main__':
	app.run(debug=True)

