-- 20-cross-join.sql

SELECT * FROM students;
SELECT * FROM courses;
-- 카르테시안 곱
SELECT
    s.name,
    c.name
FROM students s
CROSS JOIN courses c
WHERE NOT EXISTS (
    SELECT 1
    FROM students_courses sc
    WHERE sc.student_id=s.id
    AND sc.course_id=c.id
);


