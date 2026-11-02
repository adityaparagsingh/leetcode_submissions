select *,
    CASE WHEN (x+y) > z AND (y+z) > x AND (z+x) > y THEN 'Yes' ELSE 'No' END as triangle
from triangle