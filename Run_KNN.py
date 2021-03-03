import pandas as pd
import os
from process import knn, euclidean_distance

data = pd.read_csv('dataset.csv')

def recommend_movies(movie_query, k_recommendations):
    raw_movies_data = []
    with open('dataset.csv', 'r') as md:
        # Discard the first line (headings)
        next(md)

        # Read the data into memory
        for line in md.readlines():
            data_row = line.strip().split(',')
            raw_movies_data.append(data_row)

    # Prepare the data for use in the knn algorithm by picking
    # the relevant columns and converting the numeric columns
    # to numbers since they were read in as strings
    movies_recommendation_data = []
    for row in raw_movies_data:
        data_row = list(map(float, row[2:]))
        movies_recommendation_data.append(data_row)

    # Use the KNN algorithm to get the 5 movies that are most
    # similar to The Post.
    recommendation_indices, _ = knn(
        movies_recommendation_data, movie_query, k=k_recommendations,
        distance_fn=euclidean_distance, choice_fn=lambda x: None
    )

    movie_recommendations = []
    for _, index in recommendation_indices:
        movie_recommendations.append(raw_movies_data[index])

    return movie_recommendations

if __name__ == '__main__':
    the_post = [7.2, 1, 1, 0, 0, 0, 0, 1, 0] # feature vector for The Post
    recommended_movies = recommend_movies(movie_query=the_post, k_recommendations=5)

    print("===============================================================================================================")
    print(data)
    print("===============================================================================================================")
    print("\n")
    # Print recommended movie titles
    print("[Rekomendasi Film Bioskop untuk ditonton berdasarkan rating IMDb]")
    print(" ====== Menggunakan algoritma K-NN ======")
    for recommendation in recommended_movies:
        print(" > ", recommendation[0])

    print("\n")
    os.system("pause")