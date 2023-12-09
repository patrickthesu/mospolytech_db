from models import Connection
from parser import schedule_parser


conn = Connection()

def install():
    conn.reinstall()

    for group in conn.get_groups_list():
        schedule_parser(group[1], group[0])

if __name__ == '__main__':
    install()
