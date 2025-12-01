import os
from dotenv import load_dotenv
from agent import DebugAgent
from lesson_tracker import LessonTracker

def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError("Missing api key. put the api key in env file")
    
    print(" === PyMendor Debugger === ")
    
    tracker = LessonTracker()
    
    while True:
        print("\n Options:")
        print("1. Debug Python code")
        print("2. Show your top mistakes")
        print("3. Exit")
        print("4. Clear all lessons")
        
        choice = input("choose an option (1/2/3/4): ").strip()
        if not choice.isdigit():
            print("\nEnter a number, not random keyboard smashing.")
            continue
        
        if choice not in ["1", "2", "3", "4"]:
            print("\nThat option doesn't exist. Stick to 1, 2, 3 or 4.")
            continue
        
        if choice == "3":
            print("\n == Goodby ==")
            break
        
        if choice == "2":
            top = tracker.get_most_common()
            if not top:
                print("\nNo mistakes recorded yet.")
            else:
                print("\nYour most common mistakes:\n")
                for mistake, count in top:
                    print(f"- {mistake} ({count} times)")
            continue
        
        if choice == "4":
            confirm = input("\nAre you sure you want to clear all lessons? (y/n): ").strip().lower()
            if confirm == "y":
                tracker.clear_lessons()
                print("\nLessons cleared.")
            else:
                print("\nCancelled.")
            continue
        if choice == "1":
            user_code =  input("Paste your python code here and Paste Code in one line\nyou can use vs code terminal: \n\n")
            agent = DebugAgent(api_key, tracker)
            result =  agent.debug(user_code)
    
            print("\n--- RESULT ---")
            print(result)
            input("\nPress Enter to return to menu...")
        break

    
main()
