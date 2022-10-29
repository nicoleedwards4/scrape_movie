from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")
movies = soup.find_all(class_="jsx-3523802742 listicle-item")
movies = movies[::-1]

with open("movies.txt", "w") as data_file:
    for movie in movies:
        movie_num = 100 - int(movie["data-test"].split("-")[2])
        movie_name = movie.getText().split("Read Empire's review of ")[1]
        data_file.write(f"{movie_num}) {movie_name}\n")




# for item in items
#     item = item.
# print(movie_name)