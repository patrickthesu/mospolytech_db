from models import Connection
from scraper import get_students_groups_list


conn = Connection()
if not conn:
    raise Exception("Connection", "Connection is None")

def scrapp_existing_groups():
    groups_list = []
    for group in conn.get_groups_list():
        groups_list.append(group[0])

    get_students_groups_list(groups_list)

def parse_existing_groups():
    

def main():
    parse_existing_groups()

if __name__ == '__main__':
    main()
