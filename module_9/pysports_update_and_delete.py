"""pysports_join_queries.py: updates player database with new player, changes his team and info, deletes new player"""
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

#Insert player to team 1
    cursor = db.cursor()
    cursor.execute("INSERT INTO player (first_name, last_name, team_id) Values ('Smeagol', 'Shire Folk', 1);")

#print players
    cursor = db.cursor()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
    players = cursor.fetchall()
    print('\n--- DISPLAYING PLAYER AFTER INSERT ---')
    for player in players:
        print('Player ID: {}'.format(player[0]))
        print('First name: {}'.format(player[1]))
        print('Last name: {}'.format(player[2]))
        print('Team name: {}\n'.format(player[3]))
        
    input("\n\n Press any key to continue....")

#change new player to team 2
    cursor = db.cursor()
    cursor.execute("UPDATE player SET team_id =2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';")

#print players
    cursor = db.cursor()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
    players = cursor.fetchall()
    print('\n--- DISPLAYING PLAYER AFTER UPDATE ---')
    for player in players:
        print('Player ID: {}'.format(player[0]))
        print('First name: {}'.format(player[1]))
        print('Last name: {}'.format(player[2]))
        print('Team name: {}\n'.format(player[3]))
    input("\n\n Press any key to continue....")

#delete new player
    cursor = db.cursor()
    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum';")

#print players
    cursor = db.cursor()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
    players = cursor.fetchall()
    print('\n--- DISPLAYING PLAYER AFTER DELETE ---')
    for player in players:
        print('Player ID: {}'.format(player[0]))
        print('First name: {}'.format(player[1]))
        print('Last name: {}'.format(player[2]))
        print('Team name: {}\n'.format(player[3]))
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