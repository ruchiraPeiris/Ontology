from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

app.secret_key = "AS9UjjJI0J0JS9j"


@app.route('/')
def home():
    return render_template('wim_phone.html')


@app.route("/find/<string:name>/")
def hello(name):
    return render_template('found_wim_phone.html', name=name)


@app.route('/find_phone', methods=['GET'])
def search():
    try:
        user_name = request.form['username']
        brand_name = request.form['brandname']
        os = request.form['os']

        return render_template('found_wim_phone.html', name=user_name)
    except:
        return render_template('wim_phone.html')


app.add_url_rule('/find_phone', 'search', search, methods=['GET', 'POST'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
