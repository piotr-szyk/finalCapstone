'''
Data Science
TASK: Semantic Similarity (NLP)
Compulsory Task 2
Author: Piotr Szyk
Date: 1 June 2023
'''

import spacy
nlp = spacy.load("en_core_web_md")


def read_file():
    file_name = "movies.txt"
    try:
        with open(file_name, 'r') as file:
            contents = [line.strip() for line in file]
            return contents
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []


def watch_next(description):
    '''
    Take in the description of the movie as a parameter and return
    the title of the most similar movie to recommend.
    '''
    # Process the model_sentence
    model_sentence = nlp(watched_movies["description"])

    # Variables to store the maximum similarity score and movie
    max_similarity = -1
    recommended_movie = ""

    # Iterate over each movie in the movies list
    for movie in movies:
        # Calculate the similarity between the current and the model_sentence
        similarity = nlp(movie).similarity(model_sentence)

        # Update the maximum similarity and recommended movie if a higher
        # similarity is found
        if similarity > max_similarity:
            max_similarity = similarity
            recommended_movie = movie

        # Print the sentence and its similarity score
        # print(movie + " - ",  similarity)

    # Print the recommended movie with the highest similarity score
    print("Recommended movie:", recommended_movie)


movies = read_file()

# Dictionary with the watched movie titles and descriptions
watched_movies = {
                  "title": "Planet Hulk",
                  "description":
                  "Will he save their world or destroy it? When the Hulk "
                  "becomes too dangerous for the Earth, the Illuminati trick "
                  "Hulk into a shuttle and launch him into space to a planet "
                  "where the Hulk can live in peace. Unfortunately, Hulk "
                  "lands on the planet Sakaar where he is sold into slavery "
                  "and trained as a gladiator."
                  }

watch_next(watched_movies["description"])
