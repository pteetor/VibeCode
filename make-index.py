#!/usr/bin/env python3
"""
Generates index.html listing all HTML files in the current directory.
"""
import os
import re

def get_title(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return "(untitled)"

def main():
    files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
    files.sort()

    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tools</title>
</head>
<body>
    <h1>Index of HTML files</h1>
    <ul>
"""

    for filename in files:
        title = get_title(filename)
        link_text = filename[:-5]  # Remove .html
        html_content += f'        <li><a href="{filename}">{link_text}</a> <i>{title}</i></li>\n'

    html_content += """    </ul>
</body>
</html>
"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("index.html created successfully.")

if __name__ == "__main__":
    main()
