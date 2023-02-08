"""pysports_join_queries.py: """
___author___ = "Devon Lohrmann"

import mysql.connector
from mysql.connector import errorcode
#config for mysql connector
config = {
    'user': 'pysports_user',
    'password': 'D@rkNe55',
    'host': '127.0.0.1',
    'database': 'pysports',
    'raise_on_warnings': True
}
#try to connect to database
try:
    db = mysql.connector.connect(**config)
    

#print players
    cursor = db.cursor()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
    players = cursor.fetchall()
    print('\n--- DISPLAYING PLAYER RECORDS ---')
    for player in players:
        print('Player ID: {}'.format(player[0]))
        print('First name: {}'.format(player[1]))
        print('Last name: {}'.format(player[2]))
        print('Team_ID: {}\n'.format(player[3]))
    input("\n\n Press any key to continue....")

#when there is an error
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(' The supplied username or password are invalid')

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(' The specified database does not exist!')
    
    else:
        print(err)


finally:
    db.close()