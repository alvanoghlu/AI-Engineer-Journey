-- Count the number of grades for each student
SELECT s.id, s.name, COUNT(g.id) AS grade_count
FROM students s
LEFT JOIN grades g ON g.student_id = s.id
GROUP BY s.id, s.name;


-- Calculate the average grade for each student
SELECT
    s.id,
    s.name,
    ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
LEFT JOIN grades g ON g.student_id = s.id
GROUP BY s.id, s.name;

-- Select students whose average grade is above 80
SELECT
    s.id,
    s.name,
    ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
INNER JOIN grades g ON g.student_id = s.id
GROUP BY s.id, s.name
HAVING AVG(g.grade) > 80;

-- Find the highest and lowest grade for each subject
SELECT
    g.subject,
    MAX(g.grade) AS highest_grade,
    MIN(g.grade) AS lowest_grade
FROM grades g
GROUP BY g.subject;

-- Calculate average grades using only grades above 70
SELECT
    s.name,
    ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
JOIN grades g ON g.student_id = s.id
WHERE g.grade > 70
GROUP BY s.id, s.name;

-- Select students whose overall average grade is above 80
SELECT
    s.name,
    ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
JOIN grades g ON g.student_id = s.id
GROUP BY s.id, s.name
HAVING AVG(g.grade) > 80;

-- Sort students by average grade in descending order
SELECT
    s.name,
    ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
JOIN grades g ON g.student_id = s.id
GROUP BY s.id, s.name
ORDER BY avg_grade DESC;