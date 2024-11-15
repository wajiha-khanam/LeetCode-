 with cte as
 (SELECT  product_id, MAX(change_date) AS Max_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id)

select p.product_id,p.new_price as price
from products p 
join cte t on p.product_id=t.product_id and p.change_date=t.max_date
union
select product_id, 10 as price 
from products
where product_id not in (select product_id from cte)
