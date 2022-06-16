from ast import keyword
import math
from colorama import Cursor
from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
import pyodbc
from server import *

app = Flask(__name__)
# CORS(app)
server = 'adb6.database.windows.net'
database = 'assignment2'
username = 'axk3905'
password = 'Password@123'
driver = '{ODBC Driver 18 for SQL Server}'

class Main():
    cursor = ''
    data = ''
    @app.route('/')
    def index():
        cursor = connect_db()
        return render_template('index.html')

    @app.route('/q1', methods=['POST', 'GET'])
    def question1():
        if request.method == 'POST':
            mag = request.form['mag']
            cursor = connect_db()
            cursor.execute("SELECT * FROM all_month WHERE mag = ?", mag)
            data = cursor.fetchall()
            final = []
            for row in data:
                final.append([x for x in row])
            return render_template('q1.html', data=final)

    @app.route('/q2', methods=['POST', 'GET'])
    def question2():
        if request.method == 'POST':
            mag1 = request.form['mag1']
            mag2 = request.form['mag2']
            cursor = connect_db()
            cursor.execute("SELECT * FROM all_month WHERE mag BETWEEN ? AND ?", mag1, mag2)
            data = cursor.fetchall()
            final = []
            for row in data:
                final.append([x for x in row])
            return render_template('q1.html', data=final)

    @app.route('/q5', methods=['POST', 'GET'])
    def question5():
        cursor = connect_db()
        cursor.execute("SELECT * FROM all_month WHERE mag > 4.0")
        data = cursor.fetchall()
        final = []
        for row in data:
            data = row[12]
            data = data.split('T')
            print(data)
            # convert from T format from '07:26:46.040Z' to '07:26:46'
            time = data[1]
            time = time[:-4]
            time = time.split(':')
            if time[0] >= '20' and time[0] <= '08':
                final.append([x for x in row])
        return jsonify(final)

    @app.route('/q3', methods=['POST', 'GET'])
    def Task3():
        cursor = connect_db()
        if request.method == 'POST':
            latitude = float(request.form['latitude'])
            longitude = float(request.form['longitude'])
            distance = float(request.form['distance'])
            data = []
            cursor.execute("SELECT * from all_month")
            detail = cursor.fetchall()
            for r1 in detail:
                x = math.sqrt(((float(r1[1])-latitude)*2)+((float(r1[2])-longitude)*2))
                if x <= distance:
                    data.append(r1)
            return render_template('q1.html',data=data,lat=longitude,lon=longitude,dis=distance)
        return render_template('404.html')

    

    @app.route('/get_images')
    def get_images():
        return jsonify({'images': True})

    @app.route('/get_csv')
    def get_csv():
        return jsonify({'csv': True})
                
    def process_image(self, image):
        cursor = self.connect_db()

    
        

if __name__ == "__main__":

  app.logger.debug("Loading ")

  app.run(
    host='0.0.0.0', 
    port=9001, 
    debug=True)

        
    

