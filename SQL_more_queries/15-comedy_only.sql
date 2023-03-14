-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT sh.title
FROM tv_shows sh
    INNER JOIN tv_show_genres
    INNER JOIN tv_genres
ON sh.id = tv_show_genres.show_id AND tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;