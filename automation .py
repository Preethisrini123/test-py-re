import os
from datetime import datetime
folder = "C:/Users/devad/OneDrive/Desktop/file project"

today = datetime.today().strftime("%Y-%m-%d")
count = 0

for file in os.listdir(folder):
    if file.endswith(".txt"):
        old_path = os.path.join(folder, file)
        new_path = os.path.join(folder, today + "_" + file)
        os.rename(old_path, new_path)
        count += 3

print(f"Renamed: {count} files successfully on {today}")
