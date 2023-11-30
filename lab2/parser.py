import json
from random import randrange


def schedule_parser(group_id, group_name) -> None:
    filepath = f'./groups/{group_name}.json'
    with open(filepath, 'r') as file:
        students = json.loads(file.read())
        for item in students['items']:
            student = Student(
                id=None,
                full_name=item['fio'],
                student_group=group_id,
                is_leader=False,
                document=document_generator())
            student.save()
