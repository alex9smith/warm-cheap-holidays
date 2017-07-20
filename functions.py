import os
import MySQLdb
from flask import Flask, jsonify, abort, make_response, render_template, request, redirect


MYSQL_CONNECTION_NAME = os.environ.get('MYSQL_CONNECTION_NAME')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE= os.environ.get('MYSQL_DATABASE')

def connect_to_mysql():
    return MySQLdb.connect(host=MYSQL_CONNECTION_NAME, user= MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DATABASE)

def slicedict(d, s):
    return {k:v for k,v in d.iteritems() if k.startswith(s)}

def get_countries():
    cursor = connect_to_mysql().cursor()
    cursor.execute('SELECT countryName from temperatureData')
    data = cursor.fetchall()   
    return [item[0] for item in data]

def get_warm_countries(month, low_temp, high_temp):
    cursor = connect_to_mysql().cursor()
    month = 'temp' + month
    cursor.execute('SELECT countryName, ' + month + ' from temperatureData WHERE eligible = "true" AND ' + month + ' BETWEEN ' + low_temp + ' AND ' + high_temp + ' ORDER BY ' + month + ' DESC LIMIT 10')
    return cursor.fetchall()

def build_sitemap():
    sitemap = "I've not built this yet!"
    return sitemap