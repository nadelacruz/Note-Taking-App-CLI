# Note-Taking App

This app allows users to create, read, update, and delete notes stored in a database file. The app also features a command to search for messages by keyword.

## Installation

Use the command:

```bash
git clone https://github.com/nadelacruz/Note-Taking-App.git
```

### To set the API_KEY environment variable, you can run the following command in your terminal or command prompt:
```bash
export API_KEY=YOUR_API_KEY
```

## Usage
To run the app from the terminal, navigate to the directory containing the script and enter the following commands:

* run.py create note_title note_content: creates a new note with the given title and content. For example: 
```python
python run.py create "Meeting Notes" "Today we discussed the new project timeline and assigned tasks to team members."

```
* python script_name.py read note_id: reads a note with the given ID from the database file and displays its title, summary, and content. For example: 
```python
python script_name.py read 1

```
* python script_name.py update note_id --title new_title --content new_content: updates the title and content of a note with the given ID in the database file. For example: 
```python
python script_name.py update 1 --title "Updated Meeting Notes" --content "During the meeting, we decided to prioritize task A and pushed back the deadline for task B."

```
* python script_name.py delete note_id: deletes a note with the given ID from the database file. For example:
```python
python script_name.py delete 1

```
* python script_name.py update note_id --title new_title --content new_content: updates the title and content of a note with the given ID in the database file. For example: 
```python
python script_name.py update 1 --title "Updated Meeting Notes" --content "During the meeting, we decided to prioritize task A and pushed back the deadline for task B."

```
* python script_name.py delete note_id: deletes a note with the given ID from the database file. For example:
```python
python script_name.py delete 1

```
* python script_name.py search keyword: searches for notes containing the given keyword in their titles or content. For example:
```python
python script_name.py search "project timeline."

```
* python script_name.py list: lists all notes stored in the database file. For example:
```python
script_name.py list

```


## Contributing
Pull requests are welcome. For significant changes, please open an issue first to discuss what you would like to change.
