import os

folder = "dir"

if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Created folder: {folder}")

print(os.listdir(folder))
print(os.getcwd())
print(os.path.exists("harry"))
# os.remove("sample.txt")
os.rmdir(folder)