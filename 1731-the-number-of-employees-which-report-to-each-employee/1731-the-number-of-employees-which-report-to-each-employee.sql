select a.employee_id, a.name, count(b.reports_to) as reports_count, round(avg(b.age))as average_age
from employees a , employees b
where a.employee_id = b.reports_to
group by a.employee_id, a.name
order by a.employee_id
 

