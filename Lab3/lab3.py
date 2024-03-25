import Lab3.create_tables as create
import Lab3.add_values as add


def start():
    try:
        create.tables()
        add.values()
    except:
        print("Database already exists!")
