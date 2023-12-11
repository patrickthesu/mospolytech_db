from models import Connection


conn = Connection()

def install():
    conn.reinstall()

if __name__ == '__main__':
    install()
