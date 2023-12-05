import os
import psycopg2

try:
    conn = psycopg2.connect(
            host="localhost",
            database="shoe_db",
            port="8888",
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD']
    )
    print("Connected to DB")
except Exception as e:
    print("Bad Connection:", e)

# Open a cursor to perform database operations
cur = conn.cursor()

# USER table



cur.execute('DROP TABLE IF EXISTS Users CASCADE;')
cur.execute('CREATE TABLE Users ('
    'Username VARCHAR(255) PRIMARY KEY,'
    'Password VARCHAR(255) NOT NULL,'
    'Name VARCHAR(255),'
    'Birthday DATE,'
    'Email VARCHAR(255),'
    'Preferred_Size VARCHAR(50));'
)

cur.execute('DROP TABLE IF EXISTS Review CASCADE;')
cur.execute('CREATE TABLE Review ('
    'Review_ID SERIAL PRIMARY KEY,'
    'Text TEXT,'
    'Rating INTEGER);'
)

cur.execute('DROP TABLE IF EXISTS Listing CASCADE;')
cur.execute('CREATE TABLE Listing ('
    'Listing_ID SERIAL PRIMARY KEY,'
    'Size VARCHAR(50),'
    'Shoe_SKU VARCHAR(255),'
    'Description TEXT,'
    'Price DECIMAL(10, 2),'
    'Date DATE);'
)

cur.execute('DROP TABLE IF EXISTS Shoe CASCADE;')
cur.execute('CREATE TABLE Shoe ('
    'Shoe_SKU VARCHAR(255) PRIMARY KEY,'
    'Quality VARCHAR(50),'
    'Lowest_Listing_Price DECIMAL(10, 2),'
    'Manufacturer VARCHAR(255));'
)

cur.execute('DROP TABLE IF EXISTS Transaction CASCADE;')
cur.execute('CREATE TABLE Transaction ('
    'Transaction_ID SERIAL PRIMARY KEY,'
    'Sold_Price DECIMAL(10, 2),'
    'Date DATE,'
    'Buyer_Username VARCHAR(255) REFERENCES Users(Username),'
    'Seller_Username VARCHAR(255) REFERENCES Users(Username)'
');'
)

cur.execute('DROP TABLE IF EXISTS Orders CASCADE;')
cur.execute('CREATE TABLE Orders ('
    'Order_ID SERIAL PRIMARY KEY,'
    'Status VARCHAR(255),'
    'Date DATE'
');'
)

cur.execute('DROP TABLE IF EXISTS Shipment CASCADE;')
cur.execute('CREATE TABLE Shipment ('
    'Shipment_ID SERIAL PRIMARY KEY,'
    'Tracking_Number VARCHAR(255),'
    'Address VARCHAR(255),'
    'Distributor VARCHAR(255)'
');'
)

cur.execute('DROP TABLE IF EXISTS Sale_History CASCADE;')
cur.execute('CREATE TABLE Sale_History ('
    'Shoe_SKU VARCHAR(255) REFERENCES Shoe(Shoe_SKU),'
    'Name VARCHAR(255)'
');'
)

cur.execute('DROP TABLE IF EXISTS User_Reviews;')
cur.execute('CREATE TABLE User_Reviews ('
    'Username VARCHAR(255) REFERENCES Users(Username),'
    'Review_ID INTEGER REFERENCES Review(Review_ID),'
    'PRIMARY KEY (Username, Review_ID)'
');'
)

cur.execute('DROP TABLE IF EXISTS Order_Shipment;')
cur.execute('CREATE TABLE Order_Shipment ('
    'Order_ID INTEGER REFERENCES Orders(Order_ID),'
    'Shipment_ID INTEGER REFERENCES Shipment(Shipment_ID),'
    'PRIMARY KEY (Order_ID, Shipment_ID)'
');'
)

cur.execute('DROP TABLE IF EXISTS User_Buys_Listing;')
cur.execute('CREATE TABLE User_Buys_Listing ('
    'Username VARCHAR(255) REFERENCES Users(Username),'
    'Listing_ID INTEGER REFERENCES Listing(Listing_ID),'
    'PRIMARY KEY (Username, Listing_ID)'
');'
)

cur.execute('DROP TABLE IF EXISTS User_Posts_Listing;')
cur.execute('CREATE TABLE User_Posts_Listing ('
    'Username VARCHAR(255) REFERENCES Users(Username),'
    'Listing_ID INTEGER REFERENCES Listing(Listing_ID),'
    'PRIMARY KEY (Username, Listing_ID)'
');'
)