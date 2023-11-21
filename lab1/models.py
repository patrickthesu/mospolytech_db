import logging
import psycopg2

from config import DB_NAME, DB_USER, DB_PASSWORD, DB_INIT_FILE


class Connection():
    def __init__(self) -> None:
        try:
            logging.info("[MODELS] Connecting database...")
            self.connection = psycopg2.connect(
                dbname = DB_NAME,
                user = DB_USER,
                password = DB_PASSWORD,
            )
            self.cursor = self.connection.cursor()
            logging.info("[MODELS] Database succesfully connected!")
        except Exception as err:
            logging.error(f"[MODELS] {err}")
            raise Exception ("Connecting error", "error when connecting database, please check your envs or postgresql server is running")

        self.reinstall()
        try:
            self.cursor.execute("SELECT * FROM students;")
        except Exception as err:
            logging.error(f"[MODELS] {err}")
            logging.warning("[MODELS] Error when connecting database!")
            logging.info("[MODELS] Installing new database...")
            logging.info("[MODELS] Database succesfully installed!")

    def reinstall(self) -> None:
        with open(DB_INIT_FILE) as file:
            self.cursor.execute(file.read())
            self.connection.commit()

    def __del__(self) -> None:
        self.connection.close()
        logging.info("[MODELS] Closing connection to database...")


if __name__ == "__main__":
    con = Connection()
