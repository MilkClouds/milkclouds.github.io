import glob
for i in glob.glob("*.md"):
	with open(i, 'r', encoding = 'UTF-8') as file:
		r = file.read()
		r = r.replace("author: milkclouds", "author: MilkClouds")
	with open(i, 'w', encoding = 'UTF-8') as file:
		file.write(r)
