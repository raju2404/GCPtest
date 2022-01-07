# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 02:38:32 2022

@author: rajui
"""

import os
from flask import Flask, jsonify,abort
from flaskext.mysql import MySQL
from flask import Flask, jsonify, request

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Sachin@200'
app.config['MYSQL_DATABASE_DB'] = 'app_test_db'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'



mysql.init_app(app)

@app.route('/')
def hello():
    return "Hello world"


if __name__ == '__main__':
    app.run()