select b.contest_id, round(count(distinct b.user_id)/count(distinct a.user_id) * 100, 2) as percentage
from users a
join register b 
group by b.contest_id
order by percentage desc, b.contest_id asc
