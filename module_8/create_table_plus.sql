-- create table
-- AUTO_INCREMENT tells MySQL to increment the,
-- team_id by 1 each time a new record is inserted

CREATE TABLE team
(
	team_id		int			NOT NULL	auto_increment,
    team_name	VARCHAR(75)	NOT NULL,
    mascot		VARCHAR(75)	NOT NULL,
    PRIMARY KEY(team_id)
);

#PRIMARY KEY(team_id) tells MySQL that team_id is the table's,
-- primary key.