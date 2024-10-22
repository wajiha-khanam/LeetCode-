select a.customer_id, count(a.customer_id) as count_no_trans
from visits a
left join transactions b on b.visit_id = a.visit_id
where transaction_id is null
group by a.customer_id
