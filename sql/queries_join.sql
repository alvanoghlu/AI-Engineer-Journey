-- Select students with their subjects and grades using INNER JOIN
SELECT s.name, g.subject, g.grade
FROM students s
INNER JOIN grades g ON g.student_id = s.id;

-- Select all students, including those without grades
SELECT s.name, g.subject, g.grade
FROM students s
LEFT JOIN grades g ON g.student_id = s.id
WHERE g.id IS NULL;

-- Select Mathematics grades with student names
SELECT s.name, g.subject, g.grade
FROM students s
INNER JOIN grades g ON g.student_id = s.id
WHERE g.subject = 'Mathematics';

-- Demonstrate a CROSS JOIN by omitting the ON condition
SELECT s.name, g.subject, g.grade
FROM students s
CROSS JOIN grades g;