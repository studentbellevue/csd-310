CREATE TABLE team 
(
	team_id	CHAR(10)	NOT NULL,
	team_name	CHAR(10)	NOT NULL,
	mascot	CHAR(20)	NULL
);

CREATE TABLE player
(
	player_id	CHAR(10)	NOT NULL,
	first_name	CHAR(20)	NOT NULL,
	last_name	CHAR(20)	NOT NULL
);