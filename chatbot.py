#IMPORTING and CREATING SQLite DATABASE

import sqlite3
import json
from datetime import datetime #this logs the time
#
#
# Next, create code structure that executes one 
# SQL interaction to execute mutilple lines of 
# code at once. This big transaction will execute
#  all rows at once
#
timeframe = '2015-05'
sqlite3.SQLITE_TRANSACTION = []