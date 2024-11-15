select Department,Employee,Salary
from
(select b.name as department,a.name as Employee,a.salary as Salary,
dense_rank() over(partition by b.name order by a.salary desc) as ranked
from employee a
join department b on a.departmentid=b.id) as t
where ranked < 4
