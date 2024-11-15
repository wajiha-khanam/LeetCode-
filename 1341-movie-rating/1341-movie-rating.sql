(SELECT name AS results
FROM MovieRating 
JOIN Users USING(user_id)
GROUP BY name
ORDER BY COUNT(*) DESC, name
LIMIT 1)
union all
(select title as results
from movierating
join movies using(movie_id)
where extract(year_month from created_at) = 202002
group by title
order by avg(rating) desc, title
limit 1)

