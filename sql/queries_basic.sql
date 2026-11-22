-- Select grades above 80
SELECT *
FROM grades
WHERE grade > 80;


-- Select students whose names start with A
SELECT name
FROM students
WHERE name LIKE 'A%';


-- Select students whose names start with a, ignoring case
SELECT name
FROM students
WHERE name ILIKE 'a%';


-- Select the top 3 highest grades
SELECT *
FROM grades
ORDER BY grade DESC
LIMIT 3;

-- Select distinct subjects
SELECT DISTINCT subject
FROM grades;


-- Select distinct subjects
SELECT DISTINCT subject
FROM grades;


-- Select grades between 70 and 90
SELECT *
FROM grades
WHERE grade BETWEEN 70 AND 90;


-- Select grades for Mathematics and English
SELECT *
FROM grades
WHERE subject IN ('Mathematics', 'English');


-- Temporarily allow NULL values in the subject column
ALTER TABLE grades
ALTER COLUMN subject DROP NOT NULL;

-- Insert a grade with a NULL subject
INSERT INTO grades (student_id, subject, grade)
VALUES (1, NULL, 75);

-- Find rows using equality with NULL
SELECT *
FROM grades
WHERE subject = NULL;

-- Find rows using IS NULL
SELECT *
FROM grades
WHERE subject IS NULL;

-- Delete the temporary test row
DELETE FROM grades
WHERE subject IS NULL;

-- Restore the NOT NULL constraint
ALTER TABLE grades
ALTER COLUMN subject SET NOT NULL;

-- Select Mathematics grades above 80 or grades equal to 95
SELECT *
FROM grades
WHERE (subject = 'Mathematics' AND grade > 80)
   OR grade = 95;

-- Sort grades by subject ascending and grade descending
SELECT *
FROM grades
ORDER BY subject ASC, grade DESC;

-- Select student names with an alias
SELECT name AS student_name
FROM students;