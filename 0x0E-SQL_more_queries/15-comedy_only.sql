-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t.title
FROM tv_shows t
INNER JOIN tv_show_genres g
	ON g.show_id = t.id
	
	INNER JOIN tv_genres v
	ON v.id = g.genre_id
	WHERE v.name = "Comedy"
ORDER BY t.title;
