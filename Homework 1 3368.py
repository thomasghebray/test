# Thomas Ghebray
# 1889967
# Dr. Dobretsberger

import mysql.connector
from mysql.connector import Error

# This will be the command line for the user selection(s)
def user_menu():
    menu = """
    User Menu
    a - Add travel log
    d - Remove travel log
    u - Update travel log
    o - Output entire log in console 
    s - Save travel log to Database
    q - Quit 

    Choose an option:"""
    return menu

# The user will be able to select a key to modify their selection
def user_options():
    while True:
        option = input()
        # This will be the add travel menu feature
        if option == 'a': 
            travel_year = input("Enter the year of travel?")
            travel_comments = input("Would you like to add any comments?")
            travel_revisit = input("Would you be willing to revisit this location?")
            # This will be the INSERT script from mysql
            sql = "insert into log(year,comment,revisit) VALUES (%s, %s, %s)"
            value = (travel_year, travel_comments, travel_revisit)
            cursor.execute(sql, value)
            conn.commit()
        elif option == 'd': 
           # This will be the DELETE script from mysql
            sql = "DELETE FROM log WHERE year = %s"
            del_year = input("Which year would you like to remove?")
            value_2 = (del_year,)
            cursor.execute(sql, value_2)
        elif option == 'u':
            current_year = 2022
            # This will be the UPDATE script from mysql
            sql = "UPDATE log SET year = %s  WHERE  year > 2022" % current_year
            cursor.execute(sql)
            conn.commit()
            # This function will allow me to specify from the log
        elif option == "o":
            cursor.execute("SELECT * FROM log")
            row = cursor.fetchall()
            for y in row:
                print(y)

# this is how I will be establishing my sql connection
def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            password = userpw,
            database = dbname
        )
        print("\nHello Traveller!")


        # If error found, I would like to print this message
    except Error as e:
        print(f'the error {e} occured')

    return connection
# Creating connection with my specific destination 

conn = create_con('cis3368fall.csskiywpvfqh.us-east-2.rds.amazonaws.com', 'admin', 'houston713', 'cis3368db')
cursor = conn.cursor(dictionary=True)
# This will be the script to select from mysql
sql = 'select * from log'
cursor.execute(sql)
# This will execute my function
rows = cursor.fetchall()

# This allows me to print the statements I used throughout the code 
print(user_menu())
print(user_options())
