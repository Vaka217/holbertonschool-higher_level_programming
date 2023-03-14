-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT g.name
FROM tv_genres g
    INNER JOIN tv_show_genres
    INNER JOIN tv_shows
ON g.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;