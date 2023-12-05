import os
import psycopg2
from flask import (Flask, render_template, request, url_for, redirect)

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host="localhost",
                            database="shoe_db",
                            port="8888",
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Users;')
    Users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', Users=Users)

#create function for getting listing in DB


@app.route('/login/')
def login():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Users;')
    Users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('login.html', Users=Users)

@app.route('/shoelistings/')
def shoelistings():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Listing;')
    Listings = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('shoelistings.html', Listings=Listings)


@app.route('/shoecollection/')
def shoecollection():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Shoe;')
    Shoes = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('shoecollection.html', Shoes=Shoes)

@app.route('/addshoe/', methods=('GET', 'POST'))
def addshoe():
    if request.method == 'POST':
        shoe_sku = request.form['shoe_sku']
        quality = request.form['quality']
        lowest_listing_price = int(request.form['lowest_listing_price'])
        manufacturer = request.form['manufacturer']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO Shoe (Shoe_SKU, Quality, Lowest_Listing_Price, Manufacturer) VALUES (%s, %s, %s, %s)',
                    (shoe_sku, quality, lowest_listing_price, manufacturer))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('shoecollection'))

    return render_template('addshoe.html')


@app.route('/createlisting/', methods=('GET', 'POST'))
def createlisting():
    if request.method == 'POST':
        listing_id = request.form['Listing_ID']
        size = request.form['size']
        shoe_sku = request.form['Shoe_SKU']
        description = request.form['description']
        price = request.form['price']
        #date = request.form['date']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO Listing (Listing_ID, Size, Shoe_SKU, Description, Price) VALUES (%s, %s, %s, %s, %s)',
                    (listing_id, size, shoe_sku, description, price))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('shoelistings'))

    return render_template('createlisting.html')

@app.route('/adduser/', methods=('GET', 'POST'))
def adduser():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']
        birthday = request.form['birthday']
        preferred_size = request.form['preferred_size']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO Users (Username, Password, Email, Name, Birthday, Preferred_Size) VALUES (%s, %s, %s, %s, %s, %s)',
                    (username, password, email, name, birthday, preferred_size))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('adduser.html')
