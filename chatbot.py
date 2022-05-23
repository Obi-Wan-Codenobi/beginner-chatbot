#IMPORTING and CREATING SQLite DATABASE
#
import sqlite3
import json
from datetime import datetime #this logs the time
print ("***IMPORTING AND CREATING SQLITE DATABASE***")
#
#
# Next, create code structure that executes one 
# SQL interaction to execute mutilple lines of 
# code at once. This big transaction will execute
#  all rows at once
#
timeframe = '2015-05'
sqlite3.SQLITE_TRANSACTION = []
print ("CREATING SINGLE SQL CODE STRUCTURE")
#
#
# Connecting the data...
# Download your dataset and get ready to connect it
# connection = sqlite3.connect('PATH_NAME_OF_DATA/{}.db'.format(timeframe))
#
connection = sqlite3.connect('C:\\Users\Admin\Desktop\learning python AI\VSCODE\Beginner-chatbot\DATA\extracted data\RC_2015-05\{}.db'.format(timeframe))
c = connection.cursor()
#
#
# creating parent_id_, comment_id, body, name, and score into a table
#
#def create_table(): 
 #   c.execute("CREATE TABLE IF IT DOES NOT EXISTS parent_reply(parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT, comment TEXT, subreddit TEXT, unix INT, score INT)")
#def format_data(data):
 #   data = data.replace('\n',' newlinechar ').replace('\r',' newlinechar ').replace('"',"'")
 #   return data