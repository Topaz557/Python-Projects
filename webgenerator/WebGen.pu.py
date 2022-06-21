import webbrowser

f = open("basicWebsite.html", "w")
f.write("""<html>

<body>

	<h1>

	Stay Tuned for amazing summer sale!

	</h1>

</body>

</html>""")
f.close()

#open and read the file after the appending:
f = open("basicWebsite.html", "r")
print(f.read())

webbrowser.open_new_tab("basicWebsite.html")

### to create our next project we will need to import in a GUI that provides func
# to accomplish this we will do import "filename" and set the
