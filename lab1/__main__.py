from models import Connection
from scraper import get_students_groups_list
from parser import students_parser


conn = Connection()
if not conn:
    raise Exception("Connection", "Connection is None")


def scrapp_existing_groups():
    groups_list = []
    for group in conn.get_groups_list():
        groups_list.append(group[1])

    get_students_groups_list(groups_list)


def parse_existing_groups():
    for group in conn.get_groups_list():
        students_parser(group[0], group[1])


def main():
    conn.reinstall()
    scrapp_existing_groups()
    parse_existing_groups()


if __name__ == '__main__':
    main()
