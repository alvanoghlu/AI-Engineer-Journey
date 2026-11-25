
-- =========================================
-- 1. SELECT QUERIES
-- =========================================

-- 1. Retrieve all students
SELECT id, name
FROM students
ORDER BY id;

-- 2. Find grades equal to or higher than 90
SELECT student_id, subject, grade
FROM grades
WHERE grade >= 90
ORDER BY grade DESC;

-- 3. List all unique subjects
SELECT DISTINCT subject
FROM grades
ORDER BY subject;

-- 4. Find grades between 80 and 90
SELECT student_id, subject, grade
FROM grades
WHERE grade BETWEEN 80 AND 90
ORDER BY grade DESC;


-- =========================================
-- 2. JOIN QUERIES
-- =========================================

-- 5. Retrieve students with their subjects and grades
SELECT
    s.name,
    g.subject,
    g.grade
FROM students s
INNER JOIN grades g ON g.student_id = s.id
ORDER BY s.name, g.subject;

-- 6. Retrieve all students with their grades, if available
SELECT
    s.name,
    g.subject,
    g.grade
FROM students s
LEFT JOIN grades g ON g.student_id = s.id
ORDER BY s.name, g.subject;

-- 7. Find all Mathematics grades with student names
SELECT
    s.name,
    g.grade
FROM students s
INNER JOIN grades g ON g.student_id = s.id
WHERE g.subject = 'Mathematics'
ORDER BY g.grade DESC;


-- =========================================
-- 3. AGGREGATION QUERIES
-- =========================================

-- 8. Count the number of grades for each student
SELECT
    s.name,
    COUNT(g.id) AS grade_count
FROM students s
LEFT JOIN grades g ON g.student_id = s.id
GROUP BY s.id, s.name
ORDER BY grade_count DESC;

-- 9. Calculate each student's average grade
SELECT
    s.name,
    ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
INNER JOIN grades g ON g.student_id = s.id
GROUP BY s.id, s.name
ORDER BY avg_grade DESC;

-- 10. Find students whose average grade is above 85
SELECT
    s.name,
    ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
INNER JOIN grades g ON g.student_id = s.id
GROUP BY s.id, s.name
HAVING AVG(g.grade) > 85
ORDER BY avg_grade DESC;

-- 11. Find the highest and lowest grade for each subject
SELECT
    subject,
    MAX(grade) AS highest_grade,
    MIN(grade) AS lowest_grade
FROM grades
GROUP BY subject
ORDER BY subject;


-- =========================================
-- 4. SUBQUERIES AND CTE
-- =========================================

-- 12. Find grades higher than the overall average
SELECT *
FROM grades
WHERE grade > (
    SELECT AVG(grade)
    FROM grades
);

-- 13. Find students who received at least one grade of 90 or higher
SELECT s.id, s.name
FROM students s
WHERE s.id IN (
    SELECT g.student_id
    FROM grades g
    WHERE g.grade >= 90
);

-- 14. Find students who have no grades using NOT EXISTS
SELECT s.id, s.name
FROM students s
WHERE NOT EXISTS (
    SELECT 1
    FROM grades g
    WHERE g.student_id = s.id
);

-- 15. Calculate each student's average grade using a CTE
WITH student_avg AS (
    SELECT
        student_id,
        AVG(grade) AS avg_grade
    FROM grades
    GROUP BY student_id
)
SELECT
    s.name,
    ROUND(sa.avg_grade, 2) AS avg_grade
FROM students s
JOIN student_avg sa ON sa.student_id = s.id
ORDER BY sa.avg_grade DESC;

-- 16. Find students whose average is above the overall student average
WITH student_avg AS (
    SELECT
        student_id,
        AVG(grade) AS avg_grade
    FROM grades
    GROUP BY student_id
),
overall AS (
    SELECT AVG(avg_grade) AS overall_avg
    FROM student_avg
)
SELECT
    s.name,
    ROUND(sa.avg_grade, 2) AS avg_grade
FROM students s
JOIN student_avg sa ON sa.student_id = s.id
CROSS JOIN overall o
WHERE sa.avg_grade > o.overall_avg
ORDER BY sa.avg_grade DESC;


-- =========================================
-- 5. WINDOW FUNCTIONS
-- =========================================

-- 17. Compare ROW_NUMBER, RANK, and DENSE_RANK for each subject
SELECT
    s.name,
    g.subject,
    g.grade,
    ROW_NUMBER() OVER (
        PARTITION BY g.subject
        ORDER BY g.grade DESC, s.id
    ) AS row_num,
    RANK() OVER (
        PARTITION BY g.subject
        ORDER BY g.grade DESC
    ) AS rank_num,
    DENSE_RANK() OVER (
        PARTITION BY g.subject
        ORDER BY g.grade DESC
    ) AS dense_rank_num
FROM students s
JOIN grades g ON g.student_id = s.id
ORDER BY g.subject, g.grade DESC;

-- 18. Find the top two ranked students in each subject
WITH ranked AS (
    SELECT
        s.name,
        g.subject,
        g.grade,
        RANK() OVER (
            PARTITION BY g.subject
            ORDER BY g.grade DESC
        ) AS rnk
    FROM students s
    JOIN grades g ON g.student_id = s.id
)
SELECT *
FROM ranked
WHERE rnk <= 2
ORDER BY subject, rnk;

-- 19. Show each grade alongside the maximum grade in its subject
SELECT
    s.name,
    g.subject,
    g.grade,
    MAX(g.grade) OVER (
        PARTITION BY g.subject
    ) AS subject_max
FROM students s
JOIN grades g ON g.student_id = s.id
ORDER BY g.subject, g.grade DESC;

-- 20. Calculate running totals and previous grades for each student
SELECT
    s.name,
    g.subject,
    g.grade,
    SUM(g.grade) OVER (
        PARTITION BY g.student_id
        ORDER BY g.id
    ) AS student_running_total,
    LAG(g.grade) OVER (
        PARTITION BY g.student_id
        ORDER BY g.id
    ) AS prev_grade
FROM students s
JOIN grades g ON g.student_id = s.id
ORDER BY s.name, g.id;
