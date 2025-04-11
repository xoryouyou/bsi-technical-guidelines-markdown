#!/usr/bin/env python3
# filepath: generate_tr_table.py

import os
from pathlib import Path

def generate_markdown_table():
    # Define the directories to scan
    base_dirs = ['markdown/tr', 'markdown/grundschutz']
    
    # Table header
    table = "| Technical Requirement | Description |\n"
    table += "|---------------------|-------------|\n"
    
    # Scan both directories
    for base_dir in base_dirs:
        if not os.path.exists(base_dir):
            continue
            
        # Get all directories in the path
        for entry in sorted(os.listdir(base_dir)):
            full_path = os.path.join(base_dir, entry)
            if os.path.isdir(full_path):
                # Create a relative link to the directory
                # add angled brackets so spaces in links work
                relative_link = f"[{entry}](<{entry}>)"
                
                # Add row to table
                table += f"| {relative_link} | |\n"
    
    return table

def main():
    table = generate_markdown_table()
    
    with open('markdown/README.md', 'w') as f:
        f.write(table)

if __name__ == "__main__":
    main()