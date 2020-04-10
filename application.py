from flask import Flask, render_template
from azure.storage.table import TableService, Entity
table_service = TableService(account_name='cloudshell951648231', account_key='KKCvzmYv7ZIoifbmn5TpoqaynLFEqFB617TtUeEeLJWX7FnN5V1VSrflk/kLuIKtJI5aYSKmEPJ9NTObJ1g35A==')
task = {'PartitionKey': 'First', 'RowKey': '1000',
        'description': 'customer1', 'priority': 200}
table_service.update_entity('customer', task)
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! This is from Python Flask Home Page"

@app.route('/about')
def about():
    cntry = 'India'
    return "<h2> Hello World from About page %s </h2>" %cntry

@app.route('/profile/<name>')
def profile(name):
    return render_template("Profile.html",name=name)
