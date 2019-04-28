class Movie(object):
    def __init__(self, id, name, parent_id, date):
        self.id = id
        self. name = name
        self.parent_id = parent_id
        self.date = date

class Casts(object):
    def __init__(self, movie_id, person_id, job_id, role, position):
        self.movie_id = movie_id
        self.person_id = person_id
        self.job_id = job_id
        self.role = role
        self.position = position

class Person(object):
    def __init__(self, id, name, birthday, deathday, gender):
        self.id = id
        self.name = name
        self.birthday = birthday
        self.deathday = deathday
        self.gender = gender


moviesCSV, castsCSV, peopleCSV = open("./all_movies.csv"), open("./all_casts.csv"), open("./all_people.csv")

moviesList, castsList, peopleList = [], [], []

for line in moviesCSV:
    values = line.replace("\"","").split(",")
    moviesList.append(Movie(values[0],values[1],values[2],values[3]))
for line in castsCSV:
    values = line.replace("\"","").split(",")
    castsList.append(Casts(values[0],values[1],values[2],values[3], values[4]))
for line in peopleCSV:
    values = line.replace("\"","").split(",")
    peopleList.append(Person(values[0],values[1],values[2],values[3], values[4]))


year = "1970"
name = "Gimme Shelter"
#
for movie in moviesList:
    if movie.name == name and year in movie.date[:4]:
        print movie.id

movie_id = str(132)

personIdList = []
for cast in castsList:
    # print cast.movie_id
    # print cast.role
    if cast.movie_id == movie_id and cast.role is not "":
        personIdList.append(cast.person_id)

wantedPeopleList = filter(lambda x: x.id in personIdList,peopleList)
for person in wantedPeopleList:
    print person.name