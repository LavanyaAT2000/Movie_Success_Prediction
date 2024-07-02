# importing the module
import imdb
from getImdbMovieId import getImdbMovieId
import random
# creating instance of IMDb
ia = imdb.IMDb()
score_list = [7.0,8.7, 8.4, 7.0, 9.0]
def getMusicDFilmRating(id):
    print("----------music director data from imdb----------------")
    try:
        code = id
        # printing person name
        print(ia.get_person(code))
        # getting information
        actor_results = ia.get_person_filmography(code)
        print(actor_results)
        list=0;
        for index in range(2):
            movie_name = actor_results['data']['filmography']['composer'][index+1]
            print(movie_name)
            movieid=getImdbMovieId(str(movie_name))
            movie = ia.get_movie(movieid)
            list=list+movie['rating']
        return list/2  
    except:
        return random.choice(score_list)  
