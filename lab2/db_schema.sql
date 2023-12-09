CREATE TABLE student_group (
  id SERIAL PRIMARY KEY,
  name VARCHAR (10) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS telegram_user (
  telegram_id BIGINT PRIMARY KEY,
  full_name VARCHAR (255),
  student_group_id INT,
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
  name VARCHAR (50) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS time_interval (
  id SERIAL PRIMARY KEY,
  interval VARCHAR (20) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS day (
  id SERIAL PRIMARY KEY,
  name VARCHAR (20) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS schedule_item (
  id SERIAL PRIMARY KEY,
  student_group_id INT NOT NULL,
  subject_id INT NOT NULL,
  day_id INT NOT NULL,
  time_interval_id INT NOT NULL,
  FOREIGN KEY (day_id) REFERENCES day(id),
  FOREIGN KEY (subject_id) REFERENCES subject(id),
  FOREIGN KEY (time_interval_id) REFERENCES time_interval(id),
  FOREIGN KEY (student_group_id) REFERENCES student_group(id)
);


CREATE TABLE IF NOT EXISTS schedule (
  schedule_item_id INT NOT NULL,
  teacher_id INT NOT NULL,
  cabinet_id INT NOT NULL, 
  FOREIGN KEY (schedule_item_id) REFERENCES schedule_item(id),
  FOREIGN KEY (teacher_id) REFERENCES teacher(id),
  FOREIGN KEY (cabinet_id) REFERENCES cabinet(id)
);

