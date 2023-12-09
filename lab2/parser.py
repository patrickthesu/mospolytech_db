import json
from random import randrange
from models import Connection


conn = Connection()

def schedule_parser(group_name: str, group_id: int) -> None:
    filepath = f'./schedules/{group_name}.json'
    with open(filepath, 'r') as file:
        schedules = json.loads(file.read())
        for dayI, day in enumerate(schedules):
            for lesson in schedules[day]['lessons']:
                schedule_item_id = conn.insert_schedule_item(
                    dayI + 1,
                    conn.insert_time_interval(lesson["timeInterval"]),
                    conn.insert_subject(lesson["name"]),
                    group_id 
                )
                for i, teacher_name in enumerate(lesson["teachers"]):
                    teacher_name = 'Нет учителя' if teacher_name == '' else teacher_name
                    cabinet_name = 'Онлайн'
                    if len(lesson["rooms"]):
                        diff = len(lesson["rooms"]) - i - 1 
                        print(f'I: {i}\nDiff: {diff}\nLen: {len(lesson["rooms"])}\n I - diff: {i-diff}')
                        if diff < 0:
                            cabinet_name = lesson["rooms"][i+diff]
                        else:
                            cabinet_name = lesson["rooms"][i]

                    conn.insert_schedule(
                        conn.insert_teacher(teacher_name),
                        conn.insert_cabinet(cabinet_name),
                        schedule_item_id
                    )
           
if __name__ == '__main__':
    pass
