# this program makes a movie suggestion from a list of movies to watch based on another movie's description that the user watched
import spacy

# global variable
movie_list = []

# a class to represents a movies information
class Movie:

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description


# this function makes a movie suggestion based on given description
# it finds maximum similarity between all movies' descriptions and returns that move
def suggest_movie(movie_description) -> Movie:
    nlp_md = spacy.load('en_core_web_md')
    model_sentence = nlp_md(movie_description)

    max_similarity = 0
    suggestion = None

    for movie in movie_list:
        similarity = nlp_md(movie.get_description()).similarity(model_sentence)

        if max_similarity < similarity:
            max_similarity = similarity
            suggestion = movie

    return suggestion

# this function reads movies from the file
def reed_movies_file(Movie, movie_list):
    with open("./movies.txt", "r") as movies_file:
        items = movies_file.readlines()

    for item in items:
        title, description = item.strip("\n").split(" :")
        movie_list.append(Movie(title, description))


# -----------------------------------


reed_movies_file(Movie, movie_list)

result = suggest_movie("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

print(f"You may like watching {result.get_title()}")
print(f"Movie description: {result.get_description()}")