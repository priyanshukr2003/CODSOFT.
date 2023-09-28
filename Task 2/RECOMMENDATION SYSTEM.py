# Sample user profile and movie data
user_profile = {'Action': 4, 'Drama': 3, 'Comedy': 2}
movie_data = [
    {'Title': 'Movie1', 'Action': 5, 'Drama': 2, 'Comedy': 1},
    {'Title': 'Movie2', 'Action': 4, 'Drama': 3, 'Comedy': 2},
    {'Title': 'Movie3', 'Action': 2, 'Drama': 5, 'Comedy': 1},
]

# Calculate movie scores based on user profile and movie attributes
movie_scores = []
for movie in movie_data:
    score = sum(user_profile[genre] * movie[genre] for genre in user_profile)
    movie_scores.append({'Title': movie['Title'], 'Score': score})

# Sort movies by score and recommend the top ones
recommended_movies = sorted(movie_scores, key=lambda x: x['Score'], reverse=True)
print("Recommended Movies:")
for movie in recommended_movies:
    print(f"{movie['Title']} - Score: {movie['Score']}")
