-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name AS genre, count(sh.genre_id) AS number_of_shows
FROM tv_genres g, tv_show_genres sh
WHERE g.id = sh.genre_id
GROUP BY sh.genre_id, genre
ORDER BY number_of_shows DESC;