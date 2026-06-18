f = open("file.txt", "r")
text = f.read()
print(text)
f.close()

st = "Hey broo! How are you?"
f =  open("myfile.txt", "w")
f.write(st)
f.close()

st = "Hey broo! How are you?"
f =  open("myfile.txt", "a")
f.write(st)
f.close()