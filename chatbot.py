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
sql_transaction = []
print ("CREATING SINGLE SQL CODE STRUCTURE")
#
#
# Connecting the data...
# Download your dataset and get ready to connect it
# connection = sqlite3.connect('PATH_NAME_OF_DATA/{}.db'.format(timeframe))
#
connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()

def create_table(): 
    c.execute("CREATE TABLE IF NOT EXISTS parent_reply(parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT, comment TEXT, subreddit TEXT, unix INT, score INT)")

def format_data(data):
    data = data.replace("\n"," newlinechar ") .replace("/r"," newlinechar ") .replace('"',"'")
    return data

def find_parent(pid):
    try:
        sql = "SELECT comment FROM parent_reply WHERE comment_id = '{}' LIMIT 1".format(pid)
        c.execute(sql)
        result = c.fetchnone()
        if result != None:
            return result [0]
        else: return False
    except Exception as e:
        #print ("find_parent", e)
        return False


if __name__== "__main__":
    create_table()
    row_counter = 0
    paired_rows = 0

    with open("C:/Users/Admin/Desktop/learning_python/VSCODE/Beginner-chatbot/DATA/extracted data/{}/RC_{}".format(timeframe.split('-')[0], timeframe), buffer = 1000) as f:
        for row in f:
            row_counter += 1
            row = json.loads(row)
            parent_id = row['parent_id']
            body = format_data(row['body'])
            created_utc = row['created_utc']
            score = row['score']
            subreddit = row['subreddit']

            parent_data = find_parent(parent_id)

