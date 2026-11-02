select max(num) as num
from mynumbers
where num in (
    select num 
    from mynumbers
    group by num
    having Count(*) = 1
);