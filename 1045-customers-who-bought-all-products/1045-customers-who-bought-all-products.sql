SELECT customer_id 
FROM Customer 
GROUP BY customer_id 
HAVING COUNT(DISTINCT product_Key) = ( SELECT COUNT(product_Key) FROM Product)
