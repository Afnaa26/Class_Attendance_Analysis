import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the dataset
data = pd.read_csv('imdb_movie_data.csv')

# Create a directory to save the visualizations if it doesn't exist
if not os.path.exists('visuals'):
    os.makedirs('visuals')

# 1. Movie Rating Distribution (Movie names on y-axis, Rating on x-axis)
plt.figure(figsize=(10, 6))
plt.barh(data['movie'], data['rating'], color='skyblue')  # Using 'movie' as the title column
plt.title('Movie Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Movie Title')
plt.tight_layout()
plt.savefig('visuals/movie_rating_distribution.png')
plt.show()

# 2. Scatter plot: Rating vs Revenue (Aesthetic Improvements)
plt.figure(figsize=(10, 6))
plt.scatter(data['rating'], data['revenue_million'], color='green', edgecolors='black', alpha=0.6, s=100)
plt.title('Movie Rating vs Revenue')
plt.xlabel('Rating')
plt.ylabel('Revenue (in millions)')
plt.tight_layout()
plt.savefig('visuals/rating_vs_revenue.png')
plt.show()

# 3. Line plot: Average rating per year
average_rating_per_year = data.groupby('year')['rating'].mean()
plt.figure(figsize=(10, 6))
plt.plot(average_rating_per_year.index, average_rating_per_year.values, marker='o', color='orange', linestyle='-', linewidth=2)
plt.title('Average Rating per Year')
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.tight_layout()
plt.savefig('visuals/average_rating_per_year.png')
plt.show()

# 4. Histogram: Distribution of movie votes (Different colors for each bar)
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(data['votes'], bins=10, alpha=0.7)

# Apply different colors to each bar
colors = plt.cm.Paired(np.linspace(0, 1, len(patches)))
for i, patch in enumerate(patches):
    patch.set_facecolor(colors[i])

plt.title('Distribution of Movie Votes')
plt.xlabel('Number of Votes')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('visuals/distribution_of_votes.png')
plt.show()

# 5. Genre Distribution (Reverting back to Pie chart)
genre_counts = data['genre'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired(np.arange(len(genre_counts))))
plt.title('Genre Distribution')
plt.tight_layout()
plt.savefig('visuals/genre_distribution.png')
plt.show()
