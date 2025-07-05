-- create table with primary and foreign keys
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE cities(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	state_id INT,
	FOREIGN KEY(state_id) REFERENCES states(id)
);
