from flask import Flask, flash, redirect, render_template, request, session, abort
from OWL_Ready.owl_manager import *

app = Flask(__name__)

app.secret_key = "AS9UjjJI0J0JS9j"


@app.route('/')
def home():
    return render_template('wim_phone.html')


@app.route("/find/<string:name>/")
def hello(name):
    return render_template('found_wim_phone.html', name=name)


@app.route('/find_users', methods=['GET'])
def search():
    try:
        phone_price = request.form['price']

        users = findUsersByPrice(phone_price)
        return render_template('found_wim_phone.html', ph_price=phone_price, users_list=users)
    except:
        return render_template('wim_phone.html')


@app.route('/query1', methods=['GET'])
def search1():
    try:
        user_name = request.form['username']
        brand_name = request.form['brandname']
        os = request.form['os']

        return render_template('result1.html', name=user_name)
    except:
        return render_template('input_form1.html')


@app.route('/query2', methods=['GET'])
def search2():
    try:
        user_name = request.form['username']
        brand_name = request.form['brandname']
        os = request.form['os']

        return render_template('result2.html', name=user_name)
    except:
        return render_template('input_form2.html')


@app.route('/query3', methods=['GET'])
def search3():
    try:
        user_name = request.form['username']
        brand_name = request.form['brandname']
        os = request.form['os']

        return render_template('result3.html', name=user_name)
    except:
        return render_template('input_form3.html')


@app.route('/query4', methods=['GET'])
def search4():
    try:
        user_name = request.form['username']
        brand_name = request.form['brandname']
        os = request.form['os']

        return render_template('result4.html', name=user_name)
    except:
        return render_template('input_form4.html')


app.add_url_rule('/find_users', 'search', search, methods=['GET', 'POST'])
app.add_url_rule('/query1', 'search1', search1, methods=['GET', 'POST'])
app.add_url_rule('/query2', 'search2', search2, methods=['GET', 'POST'])
app.add_url_rule('/query3', 'search3', search3, methods=['GET', 'POST'])
app.add_url_rule('/query4', 'search4', search4, methods=['GET', 'POST'])

if __name__ == "__main__":
    app.run(host='localhost', port=9800)
