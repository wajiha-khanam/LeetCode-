# select name 
# from customer
# where name not in (
# select name from customer where referee_id = 2)

select name
from customer
where referee_id != 2 or referee_id is null