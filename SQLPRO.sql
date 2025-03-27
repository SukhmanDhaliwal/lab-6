CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dob DATE NOT NULL,
    amount_due DECIMAL(10,2) NOT NULL
);

INSERT INTO students (first_name, last_name, dob, amount_due) 
VALUES 
('Sukhman', 'Dhaliwal', '2000-05-15', 1500.50),
('Jaimin', 'Patel', '1999-08-22', 2000.75),
('Manpreet', 'Kaur', '2001-02-10', 1750.00),
('Mohammad', 'Ruman', '2002-11-30', 1000.25),
('Mandeep', 'Kaur', '1998-07-05', 2250.60);

SELECT * FROM students;
