-- Number of shows by genre
SELECT tv_genres AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres, tv_show_genres
WHERE tv_genre.id = tv_show_genres.genre_id
GROUP BY tv_genre.name
ORDER BY number_of_shows DESC;
