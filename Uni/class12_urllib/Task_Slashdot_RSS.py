import urllib

# rssFile = urllib.urlopen("http://rss.slashdot.org/Slashdot/slashdot")
rssFile = open("./slashshot_snipplet_rss.txt")

currentLine = rssFile.readline()
items = []

iter = 0
while currentLine:
    if "<item" in currentLine and "</item>" not in currentLine:
        items.append({})
        currentLine = rssFile.readline()
        while "</item" not in currentLine:

            if "description" in currentLine:
                # includes whole line
                items[-1]['description'] = currentLine
            if "title" in currentLine:
                # includes whole line
                items[-1]['title'] = currentLine
            currentLine = rssFile.readline()

    currentLine = rssFile.readline()

print items
print len(items)
