class Movie(object):
    def __init__(self, id, name, parent_id, date):
        self.id = id
        self. name = name
        self.parent_id = parent_id
        self.date = date

class CategoryName(object):
    def __init__(self, category_id, name, language):
        self.category_id = category_id
        self.name = name
        self.language = language

class MovieKeyword(object):
    def __init__(self, movie_id, category_id):
        self.movie_id = movie_id
        self.category_id = category_id

moviesCSV, category_names_csv, movie_keywords_csv = open("./all_movies.csv"), open("./category_names.csv"), open("./movie_keywords.csv")

moviesList, category_names_list, movie_keywords_list = [], [], []

for line in moviesCSV:
    values = line.replace("\"","").split(",")
    moviesList.append(Movie(values[0],values[1],values[2],values[3]))
for line in category_names_csv:
    values = line.replace("\"","").split(",")
    category_names_list.append(CategoryName(values[0], values[1], values[2]))
for line in movie_keywords_csv:
    values = line.replace("\"","").split(",")
    movie_keywords_list.append(MovieKeyword(values[0], values[1]))



year = "1970"
name = "Gimme Shelter"
#
for movie in moviesList:
    if movie.name == name and year in movie.date[:4]:
        print movie.id

movie_id = str(132)

# category_ids = [x for x in movie_keywords_list if x.movie_id == movie_id]
category_ids = []
for keywordsObj in movie_keywords_list:
    if keywordsObj.movie_id == movie_id:
        category_ids.append(keywordsObj.category_id.replace("\n",""))


for category in category_names_list:
    if category.category_id in category_ids:
        print category.name