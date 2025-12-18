#!/usr/bin/env python3
"""
Build script for ConvertCookie Tool
- Tạo virtual environment
- Build executable với PyInstaller
- Tạo file ZIP chứa exe + input + output
"""

import subprocess
import sys
import os
import shutil
import zipfile
from datetime import datetime

def main():
    print("🔧 ConvertCookie Build Script")
    print("=" * 40)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    venv_dir = os.path.join(base_dir, ".venv")
    source_file = "convert_cookie.py"
    output_name = "ConvertCookie"
    
    if not os.path.exists(source_file):
        print(f"❌ Không tìm thấy: {source_file}")
        sys.exit(1)
    
    # Step 1: Create venv if not exists
    if not os.path.exists(venv_dir):
        print("📦 Tạo virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
    
    # Get venv python/pip
    if sys.platform == "win32":
        venv_python = os.path.join(venv_dir, "Scripts", "python.exe")
        venv_pip = os.path.join(venv_dir, "Scripts", "pip.exe")
    else:
        venv_python = os.path.join(venv_dir, "bin", "python")
        venv_pip = os.path.join(venv_dir, "bin", "pip")
    
    # Step 2: Install PyInstaller
    print("📥 Cài đặt PyInstaller...")
    subprocess.check_call([venv_pip, "install", "pyinstaller", "-q"])
    
    # Step 3: Build
    print(f"🔨 Đang build {source_file}...")
    
    cmd = [
        venv_python, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        f"--name={output_name}",
        "--clean",
        "--noconfirm",
        source_file
    ]
    
    subprocess.check_call(cmd)
    
    # Step 4: Check result
    exe_ext = ".exe" if sys.platform == "win32" else ""
    exe_path = os.path.join("dist", output_name + exe_ext)
    
    if not os.path.exists(exe_path):
        print("❌ Build thất bại!")
        sys.exit(1)
    
    print("✅ Build thành công!")
    
    # Step 5: Create ZIP package
    print("📦 Tạo file ZIP...")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"ConvertCookie_{timestamp}.zip"
    
    # Create temp package folder
    pkg_dir = os.path.join(base_dir, "package_temp")
    if os.path.exists(pkg_dir):
        shutil.rmtree(pkg_dir)
    os.makedirs(pkg_dir)
    
    # Copy exe
    shutil.copy2(exe_path, os.path.join(pkg_dir, output_name + exe_ext))
    
    # Create input folder with add subfolder
    input_dir = os.path.join(pkg_dir, "input")
    os.makedirs(input_dir)
    add_dir = os.path.join(input_dir, "add")
    os.makedirs(add_dir)
    
    # Create sample input.txt
    with open(os.path.join(input_dir, "input.txt"), "w") as f:
        f.write("# Đặt cookie ở đây, mỗi dòng một cookie\n")
        f.write("# Format: cookie_string|password\n")
    
    # Create README in add folder
    with open(os.path.join(add_dir, "README.txt"), "w") as f:
        f.write("Đặt các file/tool cần copy vào mỗi thư mục account ở đây\n")
    
    # Create output folder
    os.makedirs(os.path.join(pkg_dir, "output"))
    
    # Create ZIP
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(pkg_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arc_name = os.path.relpath(file_path, pkg_dir)
                zf.write(file_path, arc_name)
        
        # Add empty output folder
        zf.writestr("output/.gitkeep", "")
    
    # Cleanup
    print("🧹 Dọn dẹp...")
    shutil.rmtree(pkg_dir)
    for folder in ["build", "dist", "__pycache__"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
    for f in os.listdir("."):
        if f.endswith(".spec"):
            os.remove(f)
    
    print("=" * 40)
    print(f"🎉 Hoàn thành!")
    print(f"📦 File: {zip_name}")
    print("=" * 40)

if __name__ == "__main__":
    main()
