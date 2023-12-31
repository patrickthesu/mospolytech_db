import requests
import json


def get_students_group(name: str):
    responce = requests.get(
        'https://e.mospolytech.ru/old/lk_api.php/?getStudents&search=&group=' +
        str(name) +
        '''&page=1&perpage=50&token=AO89rn45Jeklc7TSR8Fl4Z84EWi0%2FOQxDHllnRTDn%2F7\
xMTZgPEFWacFk%2BbO2lmIVpB4FZl3gw4Gl4vqwmhv0ZgAx%2BGldRn2BM7QumLDk%2BSfmN7vS\
FHkrUDHP%2FoKixIoai8Kb7U1HyFfIQmhkL%2FXWvbRfgoApC4LB9G8xrY0W8lk%3D''')

    with open(f'./groups/{name}.json', 'w', encoding="utf-8") as file:
        file.write(json.dumps(responce.json()))


def get_students_groups_list(groupList: list):
    for group in groupList:
        get_students_group(group)


if __name__ == '__main__':
    get_students_group('221-365')
