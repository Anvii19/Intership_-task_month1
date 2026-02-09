import json
from datetime import datetime


class NotesManager:
    def __init__(self):
        self.notes = []
        self.load_notes()

    def add_note(self, title, content):
        note = {
            "id": self.get_next_id(),
            "title": title,
            "content": content,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.notes.append(note)
        self.save_notes()
        return f"Note '{title}' added successfully"

    def get_next_id(self):
        if not self.notes:
            return 1
        return max(note["id"] for note in self.notes) + 1

    def save_notes(self):
        with open("notes.json", "w") as f:
            json.dump(self.notes, f, indent=2)

    def load_notes(self):
        try:
            with open("notes.json", "r") as f:
                self.notes = json.load(f)
        except FileNotFoundError:
            self.notes = []


# ---------------- MAIN / TESTING ----------------
if __name__ == "__main__":
    manager = NotesManager()
    print(manager.add_note("First Note", "This is my first note"))
