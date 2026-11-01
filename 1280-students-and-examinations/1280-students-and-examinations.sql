select stu.student_id, stu.student_name, sub.subject_name, count(ex.student_id) as attended_exams
from students stu cross join subjects sub left join examinations ex 
on sub.subject_name = ex.subject_name
and stu.student_id = ex.student_id
group by stu.student_id, stu.student_name, sub.subject_name
order by stu.student_id, stu.student_name, sub.subject_name;