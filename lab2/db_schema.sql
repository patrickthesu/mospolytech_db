CREATE TABLE student_group (
  id SERIAL PRIMARY KEY,
  name VARCHAR (10) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS telegram_user (
  telegram_id BIGINT PRIMARY KEY,
  full_name VARCHAR (255) NOT NULL,
  student_group_id INT NOT NULL,
  FOREIGN KEY (student_group_id) REFERENCES student_group(id)
);


CREATE TABLE IF NOT EXISTS subject (
  id SERIAL PRIMARY KEY,
  name VARCHAR (500) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS teacher (
  id SERIAL PRIMARY KEY,
  full_name VARCHAR (500) NOT NULL
);


CREATE TABLE IF NOT EXISTS cabinet (
  id SERIAL PRIMARY KEY,
  name VARCHAR (10) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS schedule (
  subject_id INT NOT NULL,
  teacher_id INT NOT NULL,
  cabinet_id INT NOT NULL, 
  student_group_id INT NOT NULL,
  timedate TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  FOREIGN KEY (subject_id) REFERENCES subject(id),
  FOREIGN KEY (teacher_id) REFERENCES teacher(id),
  FOREIGN KEY (cabinet_id) REFERENCES cabinet(id),
  FOREIGN KEY (student_group_id) REFERENCES student_group(id)
);
