-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tg.name, SUM(tr.rate) AS rating
FROM tv_genres tg
INNER JOIN tv_show_genres sg
	ON sg.genre_id = tg.id

	INNER JOIN tv_shows ts
		ON ts.id = sg.show_id

		INNER JOIN tv_show_ratings tr
			ON tr.show_id = ts.id
GROUP BY tg.name
ORDER BY rating DESC;
