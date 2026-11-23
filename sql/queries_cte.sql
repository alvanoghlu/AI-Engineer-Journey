-- Find grades higher than the overall average grade
SELECT *
FROM grades
WHERE grade > (
    SELECT AVG(grade)
    FROM grades
);


-- Find students who received at least one grade of 90 or higher
SELECT s.id, s.name
FROM students s
WHERE s.id IN (
    SELECT g.student_id
    FROM grades g
    WHERE g.grade >= 90
);


-- Find students who have no grades using NOT EXISTS
SELECT s.id, s.name
FROM students s
WHERE NOT EXISTS (
    SELECT 1
    FROM grades g
    WHERE g.student_id = s.id
);


-- Calculate each student's average grade using a CTE
WITH avg_grades AS (
    SELECT
        student_id,
        AVG(grade) AS avg_g
    FROM grades
    GROUP BY student_id
)
SELECT
    s.name,
    ROUND(a.avg_g, 2) AS avg_grade
FROM students s
JOIN avg_grades a ON a.student_id = s.id
ORDER BY a.avg_g DESC;


-- Find students whose average grade is above the overall student average
WITH student_avg AS (
    SELECT
        student_id,
        AVG(grade) AS avg_g
    FROM grades
    GROUP BY student_id
),
overall AS (
    SELECT AVG(avg_g) AS v
    FROM student_avg
)
SELECT
    s.name,
    ROUND(sa.avg_g, 2) AS avg_grade
FROM students s
JOIN student_avg sa ON sa.student_id = s.id
CROSS JOIN overall o
WHERE sa.avg_g > o.v
ORDER BY sa.avg_g DESC;