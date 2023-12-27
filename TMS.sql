CREATE DATABASE TaskManagementSystem;

CREATE TABLE users(
	user_id INT PRIMARY KEY,
	user_name VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(255),
    password VARCHAR(20) NOT NULL,
    confirm_password VARCHAR(20) DEFAULT 'default_value' NOT NULL
    );
    
CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    status VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

#Create new user:
INSERT INTO users(user_id,user_name,email,password,confirm_password)
VALUES (101,'Anna','anna@gmail.com','anna123','anna123');

INSERT INTO users(user_id,user_name,email,password,confirm_password)
VALUES (102,'Smith','smith@gmail.com','smith123','smith123');

INSERT INTO users(user_id,user_name,email,password,confirm_password)
VALUES (103,'Jeena','jeena@gmail.com','jeena123','jeena123');

INSERT INTO users(user_id,user_name,email,password,confirm_password)
VALUES (104,'Aaron','aaron@gmail.com','aaron123','aaron123');

INSERT INTO users(user_id,user_name,email,password,confirm_password)
VALUES (105,'Johan','johan@gmail.com','johan123','johan123');

INSERT INTO users(user_id,user_name,email,password,confirm_password)
VALUES (106,'Aadya','aadya@gmail.com','aadya123','aadya123');

SELECT * FROM users;

#Create  New Tasks:
INSERT INTO tasks (user_id, title, description, due_date,status)
VALUES (101, 'Develop a Plan', 'Create a comprehensive project roadmap 
outlining goals, tasks, and timelines.', '2023-01-09','Incomplete');

INSERT INTO tasks (user_id, title, description, due_date,status)
VALUES (102, 'Assign Tasks', 'Distribute specific responsibilities and 
assignments to team members or contributors.','2023-08-17','Incomplete');

INSERT INTO tasks (user_id, title, description, due_date,status)
VALUES (103, 'Obtain Hardware', 'Acquire the necessary physical equipment 
and infrastructure required for the project.', '2023-09-25','Incomplete');

INSERT INTO tasks (user_id, title, description, due_date,status)
VALUES (104,'Programming', 'Write, implement, and test the code according 
to the specified project requirements.', '2023-11-19','Incomplete');

INSERT INTO tasks (user_id, title, description, due_date,status)
VALUES (105,'Install Hardware', 'Physically set up and install the
hardware components in the designated environment.', '2023-03-11','Incomplete');

INSERT INTO tasks (user_id, title, description, due_date,status)
VALUES (106,'Program Test','Execute rigorous testing procedures on the 
programmed software to identify and fix potential issues.', '2023-04-23','Incomplete');

#Display a List of Tasks:
SELECT * FROM tasks;

#Display User ID:
SELECT user_id FROM users;

#Mark Task as Completed:
UPDATE tasks
SET status = 'Completed'
WHERE user_id = 103;

#Search Task:
SELECT * FROM tasks WHERE user_id=103;

#Delete a Task:
DELETE FROM tasks
WHERE use_id = 101;







