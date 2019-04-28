from urllib import urlopen, urlretrieve, quote_plus


def get_xml_lines(url):
    f = urlopen(url)

    return f.read().replace("><", ">\n<").split("\n")


def fetchArtistId(artistName):
    url = "http://musicbrainz.org/ws/2/artist/?query=artist:" + quote_plus(artistName)
    artistInfoXML = get_xml_lines(url)

    for line in artistInfoXML:
        if "artist id=" in line:
            left = line.find("artist id=") + len("artist id=") + 1
            right = line.find(" type") - 1
            return line[left:right]


def fetchArtistWorks(artistId):
    artistWorksURL = 'http://musicbrainz.org/ws/2/artist/' + artistId + '?inc=works'

    artistWorksXMLLines = get_xml_lines(artistWorksURL)

    works = []
    for i in range(len(artistWorksXMLLines)):
        if "<work-list" in artistWorksXMLLines[i]:
            while "/work-list" not in artistWorksXMLLines[i]:
                if "title" in artistWorksXMLLines[i]:
                    left = artistWorksXMLLines[i].find("<title>") + len("<title>")
                    right = artistWorksXMLLines[i].find("</title>")
                    works.append(artistWorksXMLLines[i][left:right])
                i += 1
            break
    return works

def fetchArtistTags(artistName):
    url = "http://musicbrainz.org/ws/2/artist/?query=artist:" + quote_plus(artistName)
    artistInfoXML = get_xml_lines(url)

    tags = []
    for i in range(len(artistInfoXML)):

        if "<tag-list>" in artistInfoXML[i]:
            while "</tag-list>" not in artistInfoXML[i]:
                if "name" in artistInfoXML[i]:
                    left = artistInfoXML[i].find("<name>") + len("<name>")
                    right = artistInfoXML[i].find("</name>")
                    tags.append(artistInfoXML[i][left:right])
                i += 1
            break
    return tags


print fetchArtistTags("Rammstein")
PR_artist_id = fetchArtistId("Rammstein")
print fetchArtistWorks(PR_artist_id)