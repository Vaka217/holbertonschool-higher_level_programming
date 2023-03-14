-- script that lists all cities contained in the database hbtn_0d_usa.
SELECT c.id, c.name, s.name FROM cities c INNER JOIN states s ON s.id = c.state_id ORDER BY c.id ASC;