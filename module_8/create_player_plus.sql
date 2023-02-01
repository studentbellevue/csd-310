-- create player table and set the foreign key
CREATE TABLE player 
(
	player_id	INT			NOT NULL	AUTO_INCREMENT,
    first_name	VARCHAR(75)	NOT NULL,
    last_name	VARCHAR(75) NOT NULL,
    team_id		INT			NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team, 
    FOREIGN KEY(team_id)
		REFERENCES team(team_id)
);
-- CONSTRAINT named fk_team, which contains a FOREIGN KEY of 
-- team_id.  REFERENCES is used to tell MySQL that this foreign
-- key connects to the team table by teamp_id. 