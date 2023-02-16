# Import nlp package and initialise nlp object
import spacy
nlp = spacy.load('en_core_web_md')

# Read in the movie descriptions and create dictionary of movies using label:description
with open('movies.txt', 'r') as f:
    movies = f.read().splitlines()
movie_labels = [film.split(' :')[0] for film in movies]
movie_desc = [film.split(' :')[1] for film in movies]
movie_dict = dict(zip(movie_labels, movie_desc))

# Set the test movie information and divide the title from the description
test_movie ='Planet Hulk :Will he save ' \
            'their world or destroy it? When the Hulk becomes too dangerous for the' \
            'Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a' \
            'planet where the Hulk can live in peace. Unfortunately, Hulk land on the' \
            'planet Sakaar where he is sold into slavery and trained as a gladiator.'
test_label = test_movie.split(' :')[0]
test_desc = test_movie.split(' :')[1]

# Create a token for the test movie and initialise the highest coefficient marker
test_token = nlp(test_movie)
high_coeff = 0
# Iterate through the movie dictionary, create tokens of the descriptions and calculate the coefficient of similarity
# for each movie.
for label, movie in movie_dict.items():
    movie_token = nlp(movie)
    coeff_sim = test_token.similarity(movie_token)
    # If the coefficient is higher that the previously measured pair, set the label for the most similar movie and
    # the highest coefficient
    if coeff_sim > high_coeff:
        high_coeff = coeff_sim
        most_sim_movie = label

# Print out the answer
print(f'The closest match to {test_label} is {most_sim_movie}')