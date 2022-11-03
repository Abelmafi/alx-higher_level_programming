-- Uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT name
FROM tv_genres g
INNER JOIN tv_show_genres s
        ON g.id = s.genre_id

        INNER JOIN tv_shows t
        ON t.id = s.show_id
	WHERE g.name NOT IN (
		SELECT name
		FROM tv_genres g
		INNER JOIN tv_show_genres s
        	ON g.id = s.genre_id

        	INNER JOIN tv_shows t
        	ON t.id = s.show_id
		WHERE t.title = "Dexter"
	)
ORDER BY g.name;
