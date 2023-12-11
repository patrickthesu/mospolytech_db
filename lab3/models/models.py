import logging
import psycopg2
from enum import Enum
from dataclasses import dataclass

from config import DB_NAME, DB_USER, DB_PASSWORD, DB_INIT_FILE, DB_DATA_FILE


daysDict = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
]

class Connection():
    def __init__(self) -> None:
        try:
            logging.info("[MODELS] Connecting database...")
            self.connection = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
            )
            self.cursor = self.connection.cursor()
            logging.info("[MODELS] Database succesfully connected!")
        except Exception as err:
            logging.error(f"[MODELS] {err}")
            raise Exception(
                "Connection error",
                "Error when connecting database, please check\
                your envs or postgresql server is running"
            )

    def reinstall(self) -> None:
        self.execute_file(DB_INIT_FILE)
        self.execute_file(DB_DATA_FILE)

    def get_groups_list(self) -> list | None:
        self.cursor.execute('SELECT id, name FROM student_group;')
        return self.cursor.fetchall()

    def get_telegram_user(self, telegram_id: int) -> dict | None:
        self.cursor.execute('''
            SELECT * FROM telegram_user 
            WHERE telegram_id=%(telegram_id)s;''',
            {
                'telegram_id': telegram_id
            }
        )
        
        userData = self.cursor.fetchone()
        if not userData: return

        columnNames = [d[0] for d in self.cursor.description]

        userDict = {}
        for i, name in enumerate(columnNames):
            userDict[name] = userData[i]
        return userDict


    def insert_telegram_user(self, telegram_id: int) -> dict | None:
        user = self.get_telegram_user(telegram_id)
        if user: return user
        self.cursor.execute('''
            INSERT INTO telegram_user 
            (telegram_id)
            VALUES (%(telegram_id)s);''',
            {
                'telegram_id': telegram_id,
            }
        )
        self.connection.commit()
        return

    def set_telegram_user_group(self, telegram_id: int, student_group_id: int) -> bool | None:
        user = self.get_telegram_user(telegram_id)
        if not user: return
        self.cursor.execute('''
            UPDATE telegram_user SET
            student_group_id=%(student_group_id)s
            WHERE telegram_id=%(telegram_id)s;''',
            {
                'telegram_id': telegram_id,
                'student_group_id': student_group_id,
            }
        )
        self.connection.commit()
        return True

    def set_telegram_user_name(self, telegram_id: int, name: str) -> bool | None:
        user = self.get_telegram_user(telegram_id)
        if not user: return
        self.cursor.execute('''
            UPDATE telegram_user SET
            full_name=%(full_name)s
            WHERE telegram_id=%(telegram_id)s;''',
            {
                'telegram_id': telegram_id,
                'full_name': name,
            }
        )
        self.connection.commit()
        return True


    def get_student_group_id(self, group_name: str) -> int | None:
        self.cursor.execute('''
            SELECT id FROM student_group 
            WHERE name=%(name)s;''',
            {
                'name': group_name 
            })
        id = self.cursor.fetchone()
        return id[0] if id else None

    def get_teacher_list(self):
        self.cursor.execute (f"SELECT * FROM teacher;")
        return self.cursor.fetchall()

    def get_teacher_id(self, full_name: str) -> int | None:
        self.cursor.execute('''
            SELECT id FROM teacher 
            WHERE full_name=%(full_name)s;''',
            {
                'full_name': full_name
            })
        id = self.cursor.fetchone()
        return id[0] if id else None

    def insert_teacher(self, full_name: str) -> int | None:
        id = self.get_teacher_id(full_name)
        if id: return id
        self.cursor.execute('''
            INSERT INTO teacher 
            (full_name)
            VALUES (%(full_name)s)
            RETURNING id;''',
            {
                'full_name': full_name,
            }
        )
        self.connection.commit()
        id = self.cursor.fetchone()
        return id[0] if id else None

    def delete_teacher(self, id: int) -> int | None:
        self.cursor.execute('''
            DELETE FROM teacher 
            WHERE id=(%(id)s);
            ''',
            {
                'id': id,
            }
        )
        self.connection.commit()
        return

    def get_cabinets_list(self):
        self.cursor.execute (f"SELECT * FROM cabinet;")
        return self.cursor.fetchall()

    def get_cabinet_id(self, name: str) -> int | None:
        self.cursor.execute('''
            SELECT id FROM cabinet 
            WHERE name=%(name)s;''',
            {
                'name': name 
            })
        id = self.cursor.fetchone()
        return id[0] if id else None

    def insert_cabinet(self, name: str) -> int | None:
        id = self.get_cabinet_id(name)
        if id: return id
        self.cursor.execute('''
            INSERT INTO cabinet 
            (name)
            VALUES (%(name)s)
            RETURNING id;''',
            {
                'name': name,
            }
        )
        self.connection.commit()
        id = self.cursor.fetchone()
        return id[0] if id else None

    def delete_cabinet(self, id: int) -> int | None:
        self.cursor.execute('''
            DELETE FROM cabinet 
            WHERE id=(%(id)s);
            ''',
            {
                'id': id,
            }
        )
        self.connection.commit()
        return

    def get_subjects_list(self):
        self.cursor.execute (f"SELECT * FROM subject;")
        return self.cursor.fetchall()

    def get_subject_id(self, name: str) -> int | None:
        self.cursor.execute('''
            SELECT id FROM subject 
            WHERE name=%(name)s;''',
            {
                'name': name,
            }
        )
        id = self.cursor.fetchone()
        return id[0] if id else None
    
    def insert_subject(self, name: str) -> int | None:
        id = self.get_subject_id(name)
        if id: return id
        self.cursor.execute('''
            INSERT INTO subject 
            (name)
            VALUES (%(name)s)
            RETURNING id;''',
            {
                'name': name,
            }
        )
        self.connection.commit()
        id = self.cursor.fetchone()
        return id[0] if id else None

    def delete_subject(self, id: int) -> int | None:
        self.cursor.execute('''
            DELETE FROM subject
            WHERE id=(%(id)s);
            ''',
            {
                'id': id,
            }
        )
        self.connection.commit()
        return

    def get_time_interval_id(self, interval: str) -> int | None:
        self.cursor.execute('''
            SELECT id FROM time_interval 
            WHERE interval=%(interval)s;''',
            {
                'interval': interval,
            }
        )
        id = self.cursor.fetchone()
        return id[0] if id else None
 
    def get_time_interval_list(self):
        self.cursor.execute (f"SELECT * FROM time_interval;")
        return self.cursor.fetchall()

    def get_day_list(self):
        self.cursor.execute (f"SELECT * FROM day;")
        return self.cursor.fetchall()


    def get_schedule_item_list(self) -> list:
        self.cursor.execute('''
        SELECT i.id, g.name, u.name, day.name, ti.interval FROM schedule_item i
        JOIN student_group g ON g.id=i.student_group_id
        JOIN subject u ON u.id=i.subject_id
        JOIN time_interval ti ON i.time_interval_id=ti.id
        JOIN day ON i.day_id = day.id;''')

        return self.cursor.fetchall()

    def get_schedule_list(self) -> list:
        self.cursor.execute('''
        SELECT i.id, t.full_name, c.name as cabinet_name, u.name AS subject_name, ti.interval, day.name FROM schedule s
        JOIN schedule_item i ON s.schedule_item_id = i.id
        JOIN student_group g ON g.id=i.student_group_id
        JOIN subject u ON u.id=i.subject_id
        JOIN cabinet c ON c.id=s.cabinet_id
        JOIN teacher t ON t.id=s.teacher_id
        JOIN time_interval ti ON i.time_interval_id=ti.id
        JOIN day ON i.day_id = day.id;
        ''')
        return self.cursor.fetchall()

    def get_extended_schedule_list(self) -> list:
        self.cursor.execute('''
        SELECT i.id, t.full_name, c.name as cabinet_name, ti.interval, day.name, t.id, c.id FROM schedule s
        JOIN schedule_item i ON s.schedule_item_id = i.id
        JOIN student_group g ON g.id=i.student_group_id
        JOIN subject u ON u.id=i.subject_id
        JOIN cabinet c ON c.id=s.cabinet_id
        JOIN teacher t ON t.id=s.teacher_id
        JOIN time_interval ti ON i.time_interval_id=ti.id
        JOIN day ON i.day_id = day.id;
        ''')
        return self.cursor.fetchall()


    def delete_time_interval(self, id: int) -> int | None:
        self.cursor.execute('''
            DELETE FROM time_interval
            WHERE id=(%(id)s);
            ''',
            {
                'id': id,
            }
        )
        self.connection.commit()
        return

    def insert_time_interval(self, interval: str) -> int | None:
        id = self.get_time_interval_id(interval)
        if id: return id
        self.cursor.execute('''
            INSERT INTO time_interval 
            (interval)
            VALUES (%(interval)s)
            RETURNING id;''',
            {
                'interval': interval,
            }
        )
        self.connection.commit()
        id = self.cursor.fetchone()
        return id[0] if id else None

    def delete_schedule_item(self, id: int):
        self.cursor.execute('''
            DELETE FROM schedule_item
            WHERE id=(%(id)s);
            ''',
            {
                'id': id,
            }
        )
        self.connection.commit()
        return

    def delete_schedule(self, schedule_item_id: int, teacher_id: int, cabinet_id: int):
        self.cursor.execute('''
            DELETE FROM schedule
            WHERE schedule_item_id=%(schedule_item_id)s AND
            teacher_id=%(teacher_id)s AND
            cabinet_id=%(cabinet_id)s;
            ''',
            {
                'schedule_item_id': schedule_item_id,
                'cabinet_id': cabinet_id,
                'teacher_id': teacher_id,
            }
        )
        self.connection.commit()
        return



    def insert_schedule_item(self, day_id: int, time_interval_id: int, subject_id: int, student_group_id: int) -> int | None:
        self.cursor.execute('''
            INSERT INTO schedule_item
            (day_id, time_interval_id, subject_id, student_group_id)
            VALUES (
                %(day_id)s, 
                %(time_interval_id)s, 
                %(subject_id)s, 
                %(student_group_id)s
            )
            RETURNING id;
            ''',
            {
                'day_id': day_id,
                'time_interval_id': time_interval_id,
                'subject_id': subject_id,
                'student_group_id': student_group_id,
            })
        self.connection.commit()
        id = self.cursor.fetchone()
        return id[0] if id else None


    def insert_schedule(self, teacher_id: int, cabinet_id: int, schedule_item_id: int) -> None:
        self.cursor.execute('''
            INSERT INTO schedule 
            (teacher_id, cabinet_id, schedule_item_id)
            VALUES (
                %(teacher_id)s, 
                %(cabinet_id)s, 
                %(schedule_item_id)s)
            ''',
            {
                'teacher_id': teacher_id,
                'cabinet_id': cabinet_id,
                'schedule_item_id': schedule_item_id,
            }
        )
        return

    def execute_file(self, filepath):
        with open(filepath) as file:
            self.cursor.execute(file.read())
            self.connection.commit()

    def getDaySchedule(self, day_name: str, group_id: int) -> list:
        self.cursor.execute('''
        SELECT u.name AS subject_name, c.name as cabinet_name, ti.interval, t.full_name FROM schedule s
        JOIN schedule_item i ON s.schedule_item_id = i.id
        JOIN student_group g ON g.id=i.student_group_id
        JOIN subject u ON u.id=i.subject_id
        JOIN cabinet c ON c.id=s.cabinet_id
        JOIN teacher t ON t.id=s.teacher_id
        JOIN time_interval ti ON i.time_interval_id=ti.id
        JOIN day ON i.day_id = day.id
        WHERE g.id=%(group_id)s
        AND day.name=%(day_name)s;''',
        {
            'group_id': group_id,
            'day_name': day_name 
        })
        schedule = self.cursor.fetchall() 
        if not schedule: return

        out = f'{day_name}\n\n'

        columnNames = [d[0] for d in self.cursor.description]

        scheduleList = []

        for lesson in schedule:
            lessonDict = {}
            for i, name in enumerate(columnNames):
                lessonDict[name] = lesson[i]

            scheduleList.append(lessonDict)

        return scheduleList

        #for lesson in schedule:
        #    out += f'{lesson[0]} {lesson[1]} {lesson[2]} {lesson[3]}'

        #return out


    def __del__(self) -> None:
        self.connection.close()
        logging.info("[MODELS] Closing connection to database...")


if __name__ == "__main__":
    con = Connection()
