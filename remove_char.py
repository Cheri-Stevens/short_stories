

with open(r'c:\NDCHypen.txt', 'r') as infile, \
    open(r'c:\NDCOnly.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace("-", "")
    outfile.write(data)
