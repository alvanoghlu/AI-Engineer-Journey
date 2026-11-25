-- Find the second highest distinct grade using DENSE_RANK
WITH ranked_grades AS (
    SELECT
        grade,
        DENSE_RANK() OVER (
            ORDER BY grade DESC
        ) AS rnk
    FROM grades
)
SELECT DISTINCT grade
FROM ranked_grades
WHERE rnk = 2;

-- Find the second highest distinct grade using DISTINCT and OFFSET
SELECT DISTINCT grade
FROM grades
ORDER BY grade DESC
LIMIT 1 OFFSET 1;

-- Find duplicate student grades
SELECT
    student_id,
    subject,
    grade,
    COUNT(*) AS duplicate_count
FROM grades
GROUP BY
    student_id,
    subject,
    grade
HAVING COUNT(*) > 1;

-- Count the number of duplicate groups
SELECT COUNT(*) AS duplicate_groups
FROM (
    SELECT
        student_id,
        subject,
        grade
    FROM grades
    GROUP BY student_id, subject, grade
    HAVING COUNT(*) > 1
) AS duplicates;

-- Calculate a running total of all grades
SELECT
    g.id,
    s.name,
    g.subject,
    g.grade,
    SUM(g.grade) OVER (
        ORDER BY g.id
    ) AS running_total
FROM grades g
JOIN students s ON s.id = g.student_id
ORDER BY g.id;

-- Calculate a separate running total for each student
SELECT
    s.name,
    g.subject,
    g.grade,
    SUM(g.grade) OVER (
        PARTITION BY g.student_id
        ORDER BY g.id
    ) AS student_running_total
FROM grades g
JOIN students s ON s.id = g.student_id
ORDER BY s.name, g.id;


-- Show each student's previous grade
SELECT
    s.name,
    g.subject,
    g.grade,
    LAG(g.grade) OVER (
        PARTITION BY g.student_id
        ORDER BY g.id
    ) AS prev_grade
FROM grades g
JOIN students s ON s.id = g.student_id
ORDER BY s.name, g.id;


-- Calculate the difference between current and previous grades
SELECT
    s.name,
    g.subject,
    g.grade,
    LAG(g.grade) OVER (
        PARTITION BY g.student_id
        ORDER BY g.id
    ) AS prev_grade,
    g.grade - LAG(g.grade) OVER (
        PARTITION BY g.student_id
        ORDER BY g.id
    ) AS grade_difference
FROM grades g
JOIN students s ON s.id = g.student_id
ORDER BY s.name, g.id;