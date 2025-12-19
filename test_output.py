#!/usr/bin/env python3
"""Quick test script to verify cookie output formats"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from convert_cookie import CookieConverter

# Test the converter
converter = CookieConverter()

# Process input file
input_file = os.path.join("input", "input.txt")
if not os.path.exists(input_file):
    print(f"❌ Input file not found: {input_file}")
    sys.exit(1)

count = converter.process_input_file(input_file)
print(f"✅ Found {count} cookies")

# Export
add_folder = os.path.join("input", "add")
results = converter.export_all(input_file, "output", add_folder if os.path.exists(add_folder) else None)

print(f"\n✅ Export complete!")
print(f"   Success: {results['success']}")
print(f"   Failed: {results['failed']}")
print(f"   Output: {results['output_dir']}")

# Verify first user folder
if results['success'] > 0:
    first_user = converter.cookies_data[0]['c_user']
    user_dir = os.path.join(results['output_dir'], first_user)
    
    print(f"\n📁 Checking user folder: {first_user}")
    
    files_to_check = [
        "Cookie_Headerstring.txt",
        "Cookie_NetScape.txt", 
        "Cookie_Json.txt"
    ]
    
    for filename in files_to_check:
        filepath = os.path.join(user_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"\n✅ {filename} ({len(content)} bytes)")
                # Show first 100 chars
                preview = content[:100].replace('\n', ' ').replace('\r', '')
                print(f"   Preview: {preview}...")
        else:
            print(f"\n❌ Missing: {filename}")
