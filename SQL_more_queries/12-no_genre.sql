-- list shows with no genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE genre_id = NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
