from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! This is from Python Flask Home Page"

@app.route('/about')
def about():
    return "<h2> Hello World from About page </h2>"

@app.route('/profile/<name>')
def profile(name):
    from azure.storage.table import TableService, Entity
    table_service = TableService(account_name='cloudshell669196285', account_key='RVFZCljT8OJNgHFwfqwb1nig1lLHdYgPV6a2/NTF2LVFw6tpyVZdn7GZ2NU2nX1+O8A/x1fd2Q7d1ddHqYng+g==')
    task = {'PartitionKey': 'first', 'RowKey': '004',
        'ID': '0004', 'priority': 202,'stock':65}
    table_service.insert_entity('customer', task)
    return render_template("Profile.html",name=name)
