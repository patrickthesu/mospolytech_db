from models import Connection, StudentGroup, Department
from scraper import get_students_groups_list
from parser import document_generator, students_parser


conn = Connection()
if not conn:
    raise Exception("Connection", "Connection is None")

def scrapp_existing_groups():
    groups_list = []
    for group in conn.get_groups_list():
        groups_list.append(group[0])

    get_students_groups_list(groups_list)


def parse_existing_groups():
    groups_list = []
    for group in conn.get_groups_list():
        students_parser(group[0], group[1])


def main():
    parse_existing_groups()


if __name__ == '__main__':
    main()
