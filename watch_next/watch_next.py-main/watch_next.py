# We import spacy module
import spacy

#spacy.load is used  to load the  english module
nlp = spacy.load("en_core_web_md")

# the discription of the movie is used in a multiline string
# and it is stored  under the variable description
description = """Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on planet Sakaar where he is sold into
slavery and trained as a gladiator"""

# the string value of variable description into the module is passed here
nlp_description = nlp(description)


# We define a function called similar_movie that take a movie description
# the goal is to return the title of the movie
def similar_movie(movie_description):

    # the syntax below to open and read the movies.txt and used read it
    #  using the readlines() method to read each entry and store in a list
    #  declaring a variable highest_score and assign an initial value of 0
    #  using a for loop to load each movie and description into the module
    # also conditional statements to return the highest_score which means the most similar movie
    # a split method is used to allow us to return the title of the movie only..
    with open("movies.txt", "r") as data:
        movie_data = data.readlines()
        highest_score = 0
        for movies in movie_data:
            movie_data = movies.strip()
            movie_nlp = nlp(movie_data)
            if movie_nlp.similarity(nlp_description) > highest_score:
                highest_score = movie_nlp.similarity(nlp_description)
                if highest_score == movie_nlp.similarity(nlp_description):
                    the_closest_movie = movie_nlp.text.split(":")

        return the_closest_movie[0]

# We call the function through the print method
print(similar_movie(nlp_description))