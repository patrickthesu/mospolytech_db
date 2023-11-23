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
            raise Exception ("Connection error", 
                "Error when connecting database, please check your envs or postgresql server is running"
            )
        # Check that database contain tables
        #self.reinstall()
    def get_groups_list (self) -> list | None:
        self.cursor.execute('SELECT name FROM student_group;')
        return self.cursor.fetchall()

    def insert_student (self, full_name, email, group_id, is_laeder, password) -> list | None:
        self.cursor.execute('SELECT name FROM student_group;')
        return self.cursor.fetchall()

    def reinstall(self) -> None:
        self.execute_file(DB_INIT_FILE)
        self.execute_file(DB_DATA_FILE)

    def execute_file (self, filepath):
        with open(filepath) as file:
            self.cursor.execute(file.read())
            self.connection.commit()

    def __del__(self) -> None:
        self.connection.close()
        logging.info("[MODELS] Closing connection to database...")


if __name__ == "__main__":
    con = Connection()


class DocumentType(Enum):
    russian_passport = 'Russian passport'
    foreign_passport = 'Foreign passport'
    other = 'Other'

@dataclass
class Worker(Connection):
    id: int | None
    full_name: str
    email: str
    password: str


@dataclass
class Faculty(Connection):
    id: int | None
    name: str
    dean: Worker 
    description: str


@dataclass
class Department(Connection):
    id: int | None
    name: str
    faculty: Faculty
    head: Worker


@dataclass
class StudentGroup(Connection):
    id: int | None
    name: str
    department: Department

    def get_all (self) -> list[StudentGroup]:
        self.cursor.execute('SELECT name FROM student_group;')
        return self.cursor.fetchall()


        


@dataclass
class Document(Connection):
    id: int | None
    document_type: DocumentType
    serial_number: str

    def save(self) -> None:
        self.cursor.execute(
            '''INSERT INTO document 
            (document_type, serial_number) 
            VALUES
            (:document_type, :serial_number)
            RETURNING id;''',
            {
                "document_type": str(self.document_type),
                "serial_number": self.serial_number,
            }

        )
        self.connection.commit()
        self.id = self.cursor.fetchone()


@dataclass
class Student(Connection):
    id: int | None
    full_name: str
    student_group: StudentGroup
    is_leader: bool
    document: Document

    def save(self) -> None:
        if not self.document.id:
            self.document.save()

        self.cursor.execute(
            '''INSERT INTO student 
            (full_name, student_group_id, is_leader, document_id) 
            VALUES
            (:full_name, :student_group_id, :is_leader, :document)
            RETURNING id;''',
            {
                "full_name": self.full_name,
                "student_group_id": self.student_group.id,
                "is_leader": self.is_leader,
                "document": self.document.id
            }

        )
        self.connection.commit()
        self.id = self.cursor.fetchone()
