f = open("poem.txt")
content = f.read()

if "twinkle" in content:
    print("the word is present in file")
else:
    print("the word not is present in file")

f.close()