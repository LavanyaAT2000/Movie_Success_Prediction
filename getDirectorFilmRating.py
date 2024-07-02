# importing the module
import imdb
from getImdbMovieId import getImdbMovieId

# creating instance of IMDb
ia = imdb.IMDb()

def getDirectorFilmRating(id):
    print("----------director data from imdb----------------")
    try:
        code = id
        # printing person name
        print(ia.get_person(code))
        # getting information
        actor_results = ia.get_person_filmography(code)
        print(actor_results)
        list=0;
        for index in range(1):
            movie_name = actor_results['data']['filmography']['director'][index+1]
            print(movie_name)
            movieid=getImdbMovieId(str(movie_name))
            movie = ia.get_movie(movieid)
            list=list+movie['rating']
        return list/1
    except:
        return 8.3
