-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT sh.title, g.name
FROM tv_shows sh
    LEFT JOIN tv_show_genres AS tsg ON sh.id = tsg.show_id
    LEFT JOIN tv_genres AS g ON tsg.genre_id = g.id
ORDER BY title, name;