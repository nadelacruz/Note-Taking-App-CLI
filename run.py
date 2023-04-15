import os
from note_taking_app import NoteTakingApp

API_KEY = os.environ.get('API_KEY')
if not API_KEY:
    API_KEY = input("Please enter your OpenAPI key: ")

db_file = "database.db"

app = NoteTakingApp(API_KEY, db_file)

if __name__ == "__main__":
    app.run()
