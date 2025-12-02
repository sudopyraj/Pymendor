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
            input("\nPress Enter to return to menu...")
            continue
        
        if choice == "4":
            confirm = input("\nAre you sure you want to clear all lessons? (y/n): ").strip().lower()
            if confirm == "y":
                tracker.clear_lessons()
                print("\nLessons cleared.")
            else:
                print("\nCancelled.")
            input("\nPress Enter to return to menu...")
            
            continue
            
        if choice == "1":
            print("\nHow to enter the file path correctly:\n")
            print("1. If the file is in the same folder as this program:")
            print("   Example: hello.py\n")
            print("2. If the file is inside another folder (relative path):")
            print("   Example: utils/hello.py")
            print("   Example: pymendor/test/example.py\n")
            print("3. If the file is anywhere else on your system (absolute path):")
            print("   Example: /home/kali/Desktop/hello.py")
            print("   Example: /home/kali/projects/myfolder/test.py\n")
            print("4. Make sure the path is correct and spelled properly.\n")
            while True:
                
                
                path = input("\nEnter file path : ").strip()
                    
                if  (path.startswith('"') and path.endswith('"')) or (path.startswith("'") and path.endswith("'")):
                    path = path[1:-1]
                
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        user_code = f.read()
                        break

                except Exception as e:
                    print("Congrats, something went wrong:", e)
                    continue
            agent = DebugAgent(api_key, tracker)
            result =  agent.debug(user_code)
    
            print("\n--- RESULT ---")
            print(result)
            input("\nPress Enter to return to menu...")
            
        
        

    
main()

        
