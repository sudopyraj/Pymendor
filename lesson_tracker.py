import json
import os

class LessonTracker:
    def __init__(self, filepath="history/lessons.json"):
        self.filepath = filepath
        self.lessons = self.load_lessons()

    def load_lessons(self):
        """Load lessons from JSON file. Create file if it doesn't exist."""
        if not os.path.exists(self.filepath):
            # Make sure folder exists
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            with open(self.filepath, "w") as f:
                json.dump({}, f)
            return {}

        with open(self.filepath, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def save_lessons(self):
        """Save current lessons dict to JSON."""
        with open(self.filepath, "w") as f:
            json.dump(self.lessons, f, indent=4)

    def add_lesson(self, mistake: str):
        """Record a new mistake. Count how many times it happened."""
        mistake = mistake.strip().lower()
        if mistake == "":
            return

        if mistake in self.lessons:
            self.lessons[mistake] += 1
        else:
            self.lessons[mistake] = 1

        self.save_lessons()

    def get_most_common(self, top=5):
        """Return top mistakes for tips."""
        sorted_lessons = sorted(self.lessons.items(), key=lambda x: x[1], reverse=True)
        return sorted_lessons[:top]

    def clear_lessons(self):
        """Reset all lessons (optional)."""
        self.lessons = {}
        self.save_lessons()


# Example usage:
if __name__ == "__main__":
    tracker = LessonTracker()
    tracker.add_lesson("forgot colon in python")
    tracker.add_lesson("name error variable")
    tracker.add_lesson("forgot colon in python")

    print("Top mistakes:", tracker.get_most_common())
