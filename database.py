import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
                                    id INTEGER PRIMARY KEY,
                                    title TEXT NOT NULL,
                                    content TEXT NOT NULL,
                                    summary TEXT NOT NULL
                                )''')
        self.conn.commit()

    def create_note(self, title, content, summary):
        self.cursor.execute('''INSERT INTO notes (title, content, summary) 
                                VALUES (?, ?, ?)''', (title, content, summary))
        self.conn.commit()
        return self.cursor.lastrowid

    def read_note_by_id(self, note_id):
        self.cursor.execute("SELECT * FROM notes WHERE id=?", (note_id,))
        return self.cursor.fetchone()

    def update_note_by_id(self, note_id, title, content, summary):
        self.cursor.execute('''UPDATE notes SET title=?, content=?, summary=? 
                                WHERE id=?''', (title, content, summary, note_id))
        self.conn.commit()

    def delete_note_by_id(self, note_id):
        self.cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
        self.conn.commit()

    def search_notes_by_keyword(self, keyword):
        self.cursor.execute("SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?",
                            ('%'+keyword+'%', '%'+keyword+'%'))
        return self.cursor.fetchall()

    def get_all_notes(self):
        self.cursor.execute("SELECT * FROM notes")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()