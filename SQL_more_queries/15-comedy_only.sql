--  lists all Comedy shows
SELECT tv_shows.title FROM tv_shows, tv_show_genres, tv_genres
WHERE tv_genres.name = 'Comedy' AND tv_shows.id = tv_show_genres.show_id AND tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC;
