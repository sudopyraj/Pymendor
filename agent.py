from google import genai

class DebugAgent:
    def __init__(self, api_key: str, tracker):
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-2.0-flash"
        self.tracker = tracker

    def debug(self, code: str) -> str:
        prompt = f"""
	You are a professional multi-language debugging assistant.

	Your responsibilities:
	1. Detect the programming language automatically.
	2. Identify all bugs, errors, warnings and risky patterns.
	3. Explain why each issue occurs in simple beginner-friendly terms.
	4. Provide a corrected version of the code.
	5. Suggest improvements for performance, structure, readability.

	Follow this answer format:

	== Language Detected ==
	<language>

	== Problems Found ==
	- list each issue as bullet points

	== Explanation ==
	Explain each issue clearly

	== Fixed Code ==
	<fixed code>

	== Improvements ==
	optional suggestions

	Analyse the following code:
	{code}
	"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=[prompt]
        )

        text = response.text

        # ---- Extract problems from the AI output ----
        problems = []
        capture = False

        for line in text.splitlines():
            line = line.strip()

            if line.startswith("== Problems Found"):
                capture = True
                continue

            # Stop capturing when next section starts
            if capture and line.startswith("=="):
                break

            if capture and line.startswith("- "):
                problems.append(line[2:].strip())

        # ---- Save extracted problems to lesson tracker ----
        for issue in problems:
            self.tracker.add_lesson(issue)

        return text
