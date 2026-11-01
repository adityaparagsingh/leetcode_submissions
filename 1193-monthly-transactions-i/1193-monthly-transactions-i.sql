select SUBSTR(trans_date,1,7) as month,
country,
count(id) as trans_count,
sum(CASE WHEN state = 'approved' then 1 else 0 END) as approved_count,
sum(amount) as trans_total_amount,
sum(CASE WHEN state = 'approved' then amount else 0 END) as approved_total_amount
from Transactions
group by month,country;