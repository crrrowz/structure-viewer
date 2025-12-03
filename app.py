import os

# The script that prints the project structure
PY_SCRIPT = r"""
import os

exclude = {
    ".git", ".hg", ".svn",
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    "env", "venv", ".env", ".venv",
    "node_modules", "dist", "build", ".next", ".nuxt", ".cache",
    "out", "target", ".gradle", ".idea",
    "DerivedData",
    ".dart_tool", ".packages",
    ".vscode", ".vs", ".DS_Store", "Thumbs.db",
    "logs", "log",
    ".temp", "temp", "tmp"
}

def print_structure(dir_path, prefix=""):
    items = sorted(os.listdir(dir_path))
    items = [item for item in items if item not in exclude]

    for i, item in enumerate(items):
        path = os.path.join(dir_path, item)
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "
        print(prefix + connector + item)
        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            print_structure(path, prefix + extension)

project_dir = os.getcwd()
print(project_dir + "/")
print_structure(project_dir)
"""

# WindowsApps folder (already in PATH)
winapps = os.path.expandvars(r"%USERPROFILE%\AppData\Local\Microsoft\WindowsApps")

# Paths of the files
py_path = os.path.join(winapps, "structure.py")
bat_path = os.path.join(winapps, "structure.bat")

# Create/update structure.py
with open(py_path, "w", encoding="utf-8") as f:
    f.write(PY_SCRIPT)

# Create/update structure.bat
with open(bat_path, "w", encoding="utf-8") as f:
    f.write(f"@echo off\npython \"{py_path}\" %*\n")

print("The command 'structure' is now installed or updated.")
print("Open a new terminal and type: structure")
