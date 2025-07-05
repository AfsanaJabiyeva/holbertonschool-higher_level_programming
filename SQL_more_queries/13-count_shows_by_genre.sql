-- Number of shows by genre
SELECT tv_genres AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
ORDER BY number_of_shows DESC; 
