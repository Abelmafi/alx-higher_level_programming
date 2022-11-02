--  creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_od_usa.cities(PRIMARY KEY(id), id INT NOT NULL AUTO_INCREMENT, state_id INT FOREIGN KEY(id) REFERENCES states(id) NOT NULL, VARCHAR(256) NOT NULL);
