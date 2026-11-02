select person_name 
from (
    select person_name, turn, sum(weight) over (order by turn) as cum from queue
) p1
where cum<=1000 
order by turn desc 
limit 1;