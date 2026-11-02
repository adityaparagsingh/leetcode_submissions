select user_id, count(follower_id) as followers_count
from FOllowers
group by user_id
order by user_id asc;