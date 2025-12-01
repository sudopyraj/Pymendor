import re
from google import genai

class CodeAnalyzer:
    def __init__(self, api_key: str):
        
        self.clint = genai.Client(api_key = api_key)
        
        def preprocess(self, user_input: str) -> str:
            
            cleaned = "\n".join([line.rstrip() for line in user_input.split("\n")])
            
            cleaned = cleaned.strip()
            
            if cleaned == "":
                raise ValueError("no code provided")
            
            return cleaned
        
        def detect_language(self, code: str) -> str:
            
            text = code.lower()
            
            # Python
            if any(keyword in text for keyword in ["def ", "import ", "print(", "self"]):
                return "python"

            # JavaScript
            if any(keyword in text for keyword in ["console.log", "function ", "=>", "import from"]):
                return "javascript"

            # C++
            if any(keyword in text for keyword in ["#include", "std::", "using namespace"]):
                return "cpp"

            # Java
            if any(keyword in text for keyword in ["public class", "system.out.println", "public static void main"]):
                return "java"

            # HTML
            if "<html" in text or "<body" in text or "<div" in text:
                return "html"

            # CSS
            if re.search(r"\b[a-z\-]+\s*:\s*[^;]+;", text):
                return "css"

            # SQL
            if any(keyword in text for keyword in ["select ", "insert into", "update ", "delete from", "from "]):
                return "sql"

            # Bash
            if text.startswith("#!/bin/bash") or "$" in text or "echo " in text:
                return "bash"
            
            #if everything fails
            
            try:
                response = self.client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=[f"Detect the programming language of this code. Answer ONLY with the language name:\n\n{code}"]
                )
                ai_guess = response.text.strip().lower()
                ai_guess = ai_guess.replace(".", "")
                ai_guess = ai_guess.replace("language:", "").strip()
                
                return ai_guess
            except Exception:
                return "unknown"
        
        