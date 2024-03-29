-- A database script that dumps to MySQL server
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_show.id
GROUP BY title
ORDER BY rating DESC;
