SELECT ROUND(SUM(tiv_2016),2) AS tiv_2016
FROM Insurance I1
WHERE (EXISTS (SELECT pid from Insurance I2 WHERE I2.pid!=I1.pid AND I2.tiv_2015=I1.tiv_2015) AND 
NOT EXISTS (SELECT pid from Insurance I2 WHERE I2.pid!=I1.pid AND I2.lat=I1.lat AND I2.lon=I1.lon))