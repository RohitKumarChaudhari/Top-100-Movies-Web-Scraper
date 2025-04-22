import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20250412121849/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")
movies = soup.find_all("strong")
movie_list =[]
for movie in movies:
    if (movie.getText() == "Director:" or movie.getText() == "Starring:"
            or movie.getText() == "READ MORE:" or movie.getText() == "Directors:") :
        continue
    else:
        movie_list.append(movie.getText())

movie_list.reverse()

with open("movies.txt", 'w') as file:
    for item in movie_list:
        file.write(item + '\n')

print(movie_list)




