import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")
movies_name = soup.find_all(name="h3", class_="title")
movie_titles = [movie.text for movie in movies_name]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_titles[::-1]:
        file.write(f"{movie}\n")


