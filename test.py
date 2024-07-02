# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# person id
code = "1442514"

# printing person name
print(ia.get_person(code))

# getting information
actor_results = ia.get_person_filmography(code)
print(actor_results)
# printing movie name
for index in range(10):
	movie_name = actor_results['data']['filmography']['director'][index]
	print(movie_name)
	movie = ia.get_movie('0843328')
	print(movie)
	# Print the movie's rating
	print(movie['rating'])





