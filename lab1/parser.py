import json
from random import randrange

from modeltypes import Document, DocumentType, Student, StudentGroup


def document_generator() -> Document:
    random_serial = randrange(1000, 9999)
    random_number = randrange(100000, 999999)

    return Document(
        id=None,
        document_type=DocumentType.russian_passport,
        serial_number=f'{random_serial} {random_number}'
    )
    


def students_parser(group: StudentGroup) -> None:
    with open(filepath, 'r') as file:
        students = json.loads(file.read())
        for item in students['items']: 
            student = Student(
                id=None,
                full_name=item['fio'],
                student_group=group,
                is_leader=False,
                document=document_generator()
            )
            student.save()
