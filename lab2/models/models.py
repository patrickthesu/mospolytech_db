import logging
import psycopg2
from enum import Enum
from dataclasses import dataclass

from config import DB_NAME, DB_USER, DB_PASSWORD, DB_INIT_FILE, DB_DATA_FILE


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

    def insert_teacher(self, full_name: str) -> int:
        pass
        #'''INSERT INTO teacher 
        #    (full_name)
        #    VALUES (%(full_name)s)
        #    RETURNING id;''',
        #    {
        #        "full_name": str(full_name),
        #    }


    def execute_file(self, filepath):
        with open(filepath) as file:
            self.cursor.execute(file.read())
            self.connection.commit()

    def __del__(self) -> None:
        self.connection.close()
        logging.info("[MODELS] Closing connection to database...")


if __name__ == "__main__":
    con = Connection()