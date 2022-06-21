f = open("demofile2.txt", "a")
f.write("Stay Tuned for amazing summer sale!!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
