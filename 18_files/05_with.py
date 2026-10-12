# f = open("saurabh.txt", "r")
# content = f.read()
# print(content)
# f.close()

with open("saurabh.txt", "r") as f: # context manager
    content = f.read()
    print(content)
    # No need to write f.close() because file is already closed by default when using with synax