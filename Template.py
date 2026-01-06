import re

def extract_comments(code_text):
    pattern = r"#(.*)"   # group captures comment text
    comments = re.findall(pattern, code_text)
    return comments

# Example usage
code = """
x = 10  # initialize x
y = 20  # initialize y
print(x + y)  # output result
"""

comments = extract_comments(code)

print("Extracted Comments:")
for c in comments:
    print("-", c.strip())
