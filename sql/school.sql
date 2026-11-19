DROP TABLE IF EXISTS grades, students;

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id),
    subject TEXT NOT NULL,
    grade INT CHECK (grade BETWEEN 0 AND 100)
);


INSERT INTO students (name)
VALUES
    ('Ali'),
    ('Aysel'),
    ('Murad'),
    ('Leyla'),
    ('Kamran');


INSERT INTO grades (student_id, subject, grade)
VALUES
    (1, 'Mathematics', 95),
    (1, 'English', 88),
    (1, 'Physics', 91),
    (2, 'Mathematics', 82),
    (2, 'English', 90),
    (2, 'Physics', 85),
    (3, 'Mathematics', 78),
    (3, 'English', 84),
    (3, 'Physics', 89),
    (4, 'Mathematics', 92),
    (4, 'English', 87),
    (4, 'Physics', 94),
    (5, 'Mathematics', 86),
    (5, 'English', 93),
    (5, 'Physics', 80);