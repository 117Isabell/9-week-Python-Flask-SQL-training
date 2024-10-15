
--I will create a database for CFG degree courses to store student’ information, attendance, and assignment grades starting with designing an EER diagram. The database will consist of three main tables:
--A Students Table– Stores basic student information including `student_id`, `last_name`, `first_name`, the CFG degree stream (linked to a course), and their sponsoring company.
--An Attendance Table– Tracks attendance for students across 10 classes, with fields for `student_id`, attendance status for each class, and the final attendance rate.
--A Grades Table – Stores the grades of students for their assignments and team project, with fields for `student_id`, four assignment grades, and a team project grade.
--
--I will write queries to manage data in these tables, including inserting new students, updating attendance, and retrieving grades. I will also include features like deleting to remove associated data when a student is deleted.
--The database will use various data types such as `VARCHAR` for text fields (names and courses), `INT` for numerical fields (student ID and attendance counts), and `DECIMAL` for grades. I will enforce constraints like `NOT NULL` where appropriate and ensure that each table has a properly defined primary key. Relationships between tables will be managed using foreign keys, such as linking students to their courses and grades and a stored procedure to generate personalized study reports for students, displaying their full name, stream name, all assignment grades, and average grade.

-- Part1
-- Create the database
-- CREATE DATABASE cfg_degree_training;
-- USE cfg_degree_training;


-- Part2 create 3 tables
-- Create the training_streams table
-- CREATE TABLE training_streams (
--     course_id INT PRIMARY KEY AUTO_INCREMENT,
--     course_name VARCHAR(100) NOT NULL,
--     number_of_students INT NOT NULL,
--     UNIQUE(course_name) -- Constraint: unique course names
-- );

-- Create the students table 
-- CREATE TABLE students (
--     student_id INT PRIMARY KEY AUTO_INCREMENT,
--     last_name VARCHAR(50) NOT NULL,
--     first_name VARCHAR(50) NOT NULL,
--     course_id INT,
--     sponsoring_company VARCHAR(100) DEFAULT 'None',
--     FOREIGN KEY (course_id) REFERENCES training_streams(course_id) 
-- );

-- Create the grades table
-- CREATE TABLE grades (
-- --     grade_id INT PRIMARY KEY AUTO_INCREMENT,
-- --     student_id INT,
-- --     assignment_1 DECIMAL(3,2) DEFAULT 0,
-- --     assignment_2 DECIMAL(3,2) DEFAULT 0,
-- --     assignment_3 DECIMAL(3,2) DEFAULT 0,
-- --     assignment_4 DECIMAL(3,2) DEFAULT 0,
-- --     team_project DECIMAL(3,2) DEFAULT 0,
-- --     FOREIGN KEY (student_id) REFERENCES students(student_id)
-- --     ON DELETE CASCADE -- Delete grades if a student is removed
-- -- );


-- Part3 Insert mock data into 3 tables with 3 queries
-- Insert data into training_streams
-- INSERT INTO training_streams (course_name, number_of_students)
-- VALUES
-- ('Software or Data Engineering', 2),
-- ('Data Science', 2,
-- ('Full-Stack Development', 2),
-- ('Product Management', 2);

-- Insert data into students
-- INSERT INTO students (last_name, first_name, course_id, sponsoring_company)
-- VALUES
-- ('Smith', 'John', 1, 'Company A'),
-- ('Doe', 'Jane', 2, 'Company B'),
-- ('Brown', 'Charlie', 3, 'Company C'),
-- ('Johnson', 'Emily', 4, 'Company D'),
-- ('Taylor', 'David', 1, 'Company E'),
-- ('Wilson', 'Lucy', 2, 'Company F'),
-- ('Moore', 'James', 3, 'None'),
-- ('Miller', 'Lily', 4, 'None');

-- Insert data into grades
-- INSERT INTO grades (student_id, assignment_1, assignment_2, assignment_3, assignment_4, team_project)
-- VALUES
-- (1, 85.5, 90.0, 78.5, 88.0, 92.0),
-- (2, 75.0, 80.5, 85.0, 70.5, 88.0),
-- (3, 90.0, 92.5, 95.0, 85.0, 90.0),
-- (4, 88.5, 87.0, 90.5, 93.0, 91.0),
-- (5, 85.0, 80.0, 88.0, 90.0, 85.5),
-- (6, 78.0, 85.0, 80.5, 75.5, 80.0),
-- (7, 90.0, 88.0, 85.5, 92.0, 90.5),
-- (8, 87.0, 82.0, 88.5, 84.0, 86.5);


-- Part4 queries 
-- Query 1: Get all students in Full-Stack Development
-- SELECT s.first_name, s.last_name, t.course_name
-- FROM students s
-- JOIN training_streams t ON s.course_id = t.course_id
-- WHERE t.course_name = 'Full-Stack Development'
-- ORDER BY s.last_name;

-- Query 2: Retrieve all students' grades with their course names
-- SELECT s.first_name, s.last_name, t.course_name, g.assignment_1, g.assignment_2, g.assignment_3, g.assignment_4, g.team_project
-- FROM students s
-- JOIN grades g ON s.student_id = g.student_id
-- JOIN training_streams t ON s.course_id = t.course_id
-- ORDER BY s.last_name;

-- Query 3: Retrieve all training streams
-- SELECT * FROM training_streams
-- ORDER BY course_name;

-- Query 4: Retrieve all students and their respective courses
-- SELECT s.first_name, s.last_name, t.course_name
-- FROM students s
-- JOIN training_streams t ON s.course_id = t.course_id
-- ORDER BY s.last_name;

-- Query 5: Get the full name and average grade for a particular student (e.g., student_id = 4)
-- SELECT CONCAT(s.first_name, ' ', s.last_name) AS full_name, 
--        ROUND((g.assignment_1 + g.assignment_2 + g.assignment_3 + g.assignment_4 + g.team_project) / 5, 2) AS avg_grade
-- FROM students s
-- JOIN grades g ON s.student_id = g.student_id
-- WHERE s.student_id = 4;

-- Query 6: Get the full name and average grade for all students with their training stream names
-- SELECT CONCAT(s.first_name, ' ', s.last_name) AS full_name, 
-- 	   t.course_name,
--        ROUND((g.assignment_1 + g.assignment_2 + g.assignment_3 + g.assignment_4 + g.team_project) / 5, 2) AS avg_grade
-- FROM students s
-- JOIN grades g ON s.student_id = g.student_id
-- JOIN training_streams t ON s.course_id = t.course_id
-- ORDER BY avg_grade DESC;


-- Delete a student record who has dropped out
-- DELETE FROM students WHERE student_id = 3;

-- Query 7:Find the student who has the maximum grade in the team project
-- SELECT CONCAT(s.first_name, ' ', s.last_name) AS full_name, 
--        g.team_project AS max_team_project
-- FROM students s
-- JOIN grades g ON s.student_id = g.student_id
-- WHERE g.team_project = (SELECT MAX(team_project) FROM grades);

-- Query 8: Find the student with the highest average grade
-- SELECT CONCAT(s.first_name, ' ', s.last_name) AS full_name, 
--        ROUND((g.assignment_1 + g.assignment_2 + g.assignment_3 + g.assignment_4 + g.team_project) / 5, 2) AS avg_grade
-- FROM students s
-- JOIN grades g ON s.student_id = g.student_id
-- ORDER BY avg_grade DESC
-- LIMIT 1;


-- Part5 A Stored Procedure to get a report for a student with a certain id 
-- DELIMITER //

-- CREATE PROCEDURE GetStudentReport(IN studentID INT)
-- BEGIN
--     SELECT CONCAT(s.first_name, ' ', s.last_name) AS full_name,
--            t.course_name,
--            g.assignment_1,
--            g.assignment_2,
--            g.assignment_3,
--            g.assignment_4,
--            g.team_project,
--            ROUND((g.assignment_1 + g.assignment_2 + g.assignment_3 + g.assignment_4 + g.team_project) / 5, 2) AS avg_grade
--     FROM students s
--     JOIN grades g ON s.student_id = g.student_id
--     JOIN training_streams t ON s.course_id = t.course_id
--     WHERE s.student_id = studentID;
-- END //

-- DELIMITER ;


-- Call the stored procedure with a desired student id
-- CALL GetStudentReport(4);  





