import os
import locale
# import tests.twitter_test as twitter_test
# locale.setlocale(locale.LC_ALL, '')
from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__) #create a Flask instance

@app.route('/', methods=['GET'])
def input():
    if request.method == 'GET':
        return render_template('index.html')
    

# auth = twitter_test.OAuthHandler("Bearer Token here")
# api = twitter_test.API(auth)
