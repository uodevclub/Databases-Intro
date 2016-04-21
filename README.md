# Spring 2016 Week 3 - How to Set Up a Database
That server-side Flask application from Week 2? We are adding a database to that to hold the data retrieved from calls to Twitter!

### Introduction
Today we will be making a server-side program using [Flask](http://flask.pocoo.org/ "Flask Site"), which is a Python microweb framework that makes it easy to get a server up and running.

### Setting Up

First, you want to create a folder on your local computer where your project will "live". Go ahead and clone the repository "Server-Side" if you want a good starting point. If you don't have virtual environment for Python and Flask installed already, go ahead and follow the Server-Side tutorial to install them. 

Fire up your virtual environment using the command `source <venv name>\bin\activate`. Once in your virtual environment, install psycopg2, Python tool for PostgreSQL.
```
pip install psycopg2
```
You will need to have PostgreSQL installed on your machine if you don't already. Go to http://www.postgresql.org/download/ and download the right version.
For macs, you should export Postgresql to your path by running `export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin` from your terminal.

Once you have Postgres installed, go ahead start it up. Run `psql` to enter into the command line tool so that we can make a user and database. 
```
create user <username> with password '<password>';
create database <db name> owner <username> encoding 'utf-8';
```
Keep in mind that in the psql shell you have to end commands with a semi-colon!
If you are using the starter project from this repo, you should open up the CONFIG.py file and add in the relevant information. 

In the app.py file, you will see that we connect to the database with the command.
`db_connect = psycopg2.connect(database='<database name>',user='<user you created>',password='<password you created for user>')`

Look at the tables we create in the app.py file for Users, and go ahead and put a test "user" in your database:
	cursor.execute("INSERT INTO Users ( name, username,followers_count) VALUES (%s, %s,%s)",("Hannah Smith", "hannah5th",96))
	
Now if you go into the psql shell, you will see that the user is shown in the "Users" table. Some useful commands for the psql shell are:
_\list:_ list all databases
_\dt:_ show tables in current database
_select * from <table name;_ list all entries in table
