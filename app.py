import os

# قائمة الملفات أو المجلدات المراد استثناؤها
exclude = {".git", "node_modules", "__pycache__"}  # يمكنك إضافة أي أسماء أخرى

def print_structure(dir_path, prefix=""):
    items = sorted(os.listdir(dir_path))
    # استبعاد العناصر الغير مرغوب فيها
    items = [item for item in items if item not in exclude]

    for i, item in enumerate(items):
        path = os.path.join(dir_path, item)
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "
        print(prefix + connector + item)
        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            print_structure(path, prefix + extension)


# ضع هنا مسار مشروعك
project_dir = "VidScholar-share-wxt"
print(project_dir + "/")
print_structure(project_dir)
