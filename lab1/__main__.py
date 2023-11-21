from models import Connection
from parser import get_students_groups_list


def main():
    conn = Connection()
    
    groups_list = []
    for group in conn.get_groups_list():
        groups_list.append(group[0])

    get_students_groups_list(groups_list)

if __name__ == '__main__':
    main()
