-- Compare ROW_NUMBER, RANK, and DENSE_RANK
SELECT
    s.name,
    g.subject,
    g.grade,
    ROW_NUMBER() OVER (
        PARTITION BY g.subject
        ORDER BY g.grade DESC
    ) AS rn,
    RANK() OVER (
        PARTITION BY g.subject
        ORDER BY g.grade DESC
    ) AS rnk,
    DENSE_RANK() OVER (
        PARTITION BY g.subject
        ORDER BY g.grade DESC
    ) AS drnk
FROM students s
JOIN grades g ON g.student_id = s.id
ORDER BY g.subject, g.grade DESC;

-- Find the top 2 ranked students in each subject
WITH ranked AS (
    SELECT
        s.name,
        g.subject,
        g.grade,
        DENSE_RANK() OVER (
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

-- Find the maximum grade for each subject using GROUP BY
SELECT
    g.subject,
    MAX(g.grade) AS subject_max
FROM grades g
GROUP BY g.subject;

-- Show each student's grade alongside the maximum grade in their subject
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


-- Calculate the difference between each grade and the subject maximum
SELECT
    s.name,
    g.subject,
    g.grade,
    MAX(g.grade) OVER (
        PARTITION BY g.subject
    ) AS subject_max,
    g.grade - MAX(g.grade) OVER (
        PARTITION BY g.subject
    ) AS difference
FROM students s
JOIN grades g ON g.student_id = s.id
ORDER BY g.subject, g.grade DESC;

-- Calculate a running total of all grades
SELECT
    id,
    subject,
    grade,
    SUM(grade) OVER (
        ORDER BY id
    ) AS running_total
FROM grades
ORDER BY id;