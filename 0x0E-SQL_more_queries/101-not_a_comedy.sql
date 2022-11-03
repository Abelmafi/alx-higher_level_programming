-- 
SELECT DISTINCT ts.title
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg
	ON ts.id = tsg.show_id

	LEFT JOIN tv_genres tg
	ON tsg.genre_id = tg.id
	WHERE ts.title NOT IN (
		SELECT title
		FROM tv_shows ts
		LEFT JOIN tv_show_genres tsg
			ON tsg.show_id = ts.id

			LEFT JOIN tv_genres tg
			ON tg.id = tsg.genre_id
			WHERE tg.name = "Comedy"
		)
ORDER BY ts.title;
