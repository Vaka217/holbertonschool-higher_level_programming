-- script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT ts.title, tsg.genre_id
FROM tv_shows ts
    LEFT JOIN tv_show_genres tsg
    ON ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id;