SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE DATEDIFF(day, activity_date, '2019-07-27') BETWEEN 0 AND 29
GROUP BY activity_date;
