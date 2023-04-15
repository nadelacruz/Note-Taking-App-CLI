import openai
import argparse
from database import Database
from note import Note


def generate_summary(content):
    model_engine = "text-ada-001"
    prompt = (f"Please summarize the following text:\n"
              f"{content}\n\n"
              f"Summary:")
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5
    )
    summary = response.choices[0].text.strip()
    return summary


class NoteTakingApp:
    def __init__(self, api_key, db_file):
        openai.api_key = api_key
        self.db = Database(db_file)
        self.parser = argparse.ArgumentParser(description='The Note Taking App is a command-line interface (CLI) tool designed for efficient note-taking and organization. With its intuitive commands, you can create, read, update, and delete notes stored in a database file. Additionally, you can search for notes by keyword. The app also features an AI-powered summarization tool that generates a summary of your notes with just a few keystrokes, saving you time and effort. Whether you\'re a student, professional, or just someone who likes to keep their thoughts organized, the Note Taking App is the perfect tool for simplifying your note-taking process.')

        subparsers = self.parser.add_subparsers(title='Commands', dest='command')

        # create command
        create_parser = subparsers.add_parser('create', help='create a new note stored in the database file')
        create_parser.add_argument('title', type=str, help='title of the note')
        create_parser.add_argument('content', type=str, help='content of the note')

        # read command
        read_parser = subparsers.add_parser('read', help='read a note stored in the database file')
        read_parser.add_argument('note_id', type=int, help='ID of the note to read')

        # update command
        update_parser = subparsers.add_parser('update', help='update a note stored in the database file')
        update_parser.add_argument('note_id', type=int, help='ID of the note to update')
        update_parser.add_argument('--title', type=str, help='new title for the note')
        update_parser.add_argument('--content', type=str, help='new content for the note')

        # delete command
        delete_parser = subparsers.add_parser('delete', help='delete a note stored in the database file')
        delete_parser.add_argument('note_id', type=int, help='ID of the note to delete')

        # search command
        search_parser = subparsers.add_parser('search', help='search for a note stored in the database file')
        search_parser.add_argument('keyword', type=str, help='keyword to search for in the notes')

        # list command
        list_parser = subparsers.add_parser('list', help='list all notes stored in the database file')

    def run(self):
        args = self.parser.parse_args()

        if args.command == 'create':
            self.create_note(args.title, args.content)
        elif args.command == 'read':
            self.read_note_by_id(args.note_id)
        elif args.command == 'update':
            self.update_note_by_id(args.note_id, args.title, args.content)
        elif args.command == 'delete':
            self.delete_note_by_id(args.note_id)
        elif args.command == 'search':
            self.search_notes_by_keyword(args.keyword)
        elif args.command == 'list':
            self.list_all_notes()

    def create_note(self, title, content):
        summary = generate_summary(content)
        note = Note(title, content, summary)
        note_id = self.db.create_note(note.title, note.content, note.summary)
        print(f"Note created with ID {note_id}")

    def read_note_by_id(self, note_id):
        note_data = self.db.read_note_by_id(note_id)
        if note_data is not None:
            note = Note(*note_data[1:])
            print(f"Title: {note.title}\nSummary: {note.summary}\nContent: {note.content}")
        else:
            print(f"Note with ID {note_id} not found.")

    def update_note_by_id(self, note_id, title=None, content=None):
        note_data = self.db.read_note_by_id(note_id)
        if note_data is not None:
            note = Note(*note_data[1:])
            if title is None:
                title = note.title
            if content is None:
                content = note.content
            summary = generate_summary(content)

            self.db.update_note_by_id(note_id, title, content, summary)
            print(f"Note with ID {note_id} updated.")
        else:
            print(f"Note with ID {note_id} not found.")

    def delete_note_by_id(self, note_id):
        note_data = self.db.read_note_by_id(note_id)
        if note_data is not None:
            self.db.delete_note_by_id(note_id)
            print(f"Note with ID {note_id} deleted.")
        else:
            print(f"Note with ID {note_id} not found.")

    def search_notes_by_keyword(self, keyword):
        note_data_list = self.db.search_notes_by_keyword(keyword)
        if len(note_data_list) > 0:
            for note_data in note_data_list:
                note = Note(*note_data[1:])
                print(f"ID: {note_data[0]}\nTitle: {note.title}\nSummary: {note.summary}\n")
        else:
            print(f"No notes found with keyword '{keyword}'.")

    def list_all_notes(self):
        note_data_list = self.db.get_all_notes()
        if len(note_data_list) > 0:
            for note_data in note_data_list:
                note = Note(*note_data[1:])
                print(f"ID: {note_data[0]}\nTitle: {note.title}\nSummary: {note.summary}\n")
        else:
            print("No notes found.")

