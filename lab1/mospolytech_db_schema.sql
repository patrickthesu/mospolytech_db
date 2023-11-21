CREATE TABLE worker (
id SERIAL PRIMARY KEY,
full_name VARCHAR (255) NOT NULL,
email VARCHAR (255) NOT NULL UNIQUE,
password VARCHAR (255) NOT NULL
);

CREATE TABLE faculty (
id SERIAL PRIMARY KEY,
name VARCHAR (255) NOT NULL UNIQUE,
dean_id INT NOT NULL,
description TEXT,
FOREIGN KEY (dean_id) REFERENCES worker(id)
);

CREATE TABLE department (
id SERIAL PRIMARY KEY,
name VARCHAR (255) NOT NULL UNIQUE,
faculy_id INT NOT NULL,
head_of_department_id INT NOT NULL,
FOREIGN KEY (faculy_id) REFERENCES faculty(id),
FOREIGN KEY (head_of_department_id) REFERENCES worker(id)
);

CREATE TABLE student_group (
id SERIAL PRIMARY KEY,
name VARCHAR (10) NOT NULL UNIQUE,
department_id INT NOT NULL,
FOREIGN KEY (department_id) REFERENCES department(id)
);

CREATE TABLE student (
id SERIAL PRIMARY KEY,
full_name VARCHAR (255) NOT NULL,
password VARCHAR (255) NOT NULL,
student_group_id INT NOT NULL,
is_leader BOOLEAN NOT NULL DEFAULT FALSE,
FOREIGN KEY (student_group_id) REFERENCES student_group(id)
);
