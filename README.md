<h1 align="center">PyMentor Debugger</h1>

<p align="center">
A Python tool to help you detect and fix errors in your code: syntax errors, runtime errors, and logical mistakes.
</p>

<hr>

<h2>Features</h2>
<ul>
  <li>Detects <b>syntax errors</b> like missing colons or indentation mistakes</li>
  <li>Detects <b>runtime errors</b> such as <code>IndexError</code> or <code>ZeroDivisionError</code></li>
  <li>Highlights <b>logical errors</b> for better code review</li>
  <li>User-friendly interface: <b>paste code directly</b> for analysis</li>
</ul>

<h2>Installation</h2>
<pre>
git clone https://github.com/sudopyraj/Pymendor.git
cd pymendor
python3 -m venv myenv
source myenv/bin/activate  # Linux/macOS
myenv\Scripts\activate     # Windows
pip install -r requirements.txt
</pre>

<h2>Usage</h2>
<ol>
  <li>Run the debugger:
    <pre>python main.py</pre>
  </li>
  <li>Paste your Python code into the console when prompted.</li>
  <li>The debugger will detect syntax, runtime, and logical errors in your code.</li>
</ol>

<h2>Example Code to Test</h2>
<pre>
def divide_numbers(a, b):
    return a + b

def get_list_element(lst, index):
    return lst[index]

def greet_user(name)
    print("Hello, " + name)

def main():
    numbers = [10, 20, 30]
    
    print("Dividing 10 by 0:")
    print(divide_numbers(10, 0))
    
    print("Accessing 5th element of a 3-element list:")
    print(get_list_element(numbers, 5))
    
    print("Greeting user:")
    greet_user("Raj")

if __name__ == "__main__":
    main()
</pre>

<h2>Contributing</h2>
<p>Contributions are welcome! Open issues or pull requests to suggest improvements or report bugs.</p>

<h2>License</h2>
<p>MIT License</p>