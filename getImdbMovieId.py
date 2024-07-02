import imdb

# create an instance of the IMDb class
ia = imdb.IMDb()



def getImdbMovieId(name):
    # search for the movie by title
    movie_results = ia.search_movie(name)
    # extract the IMDb ID of the first search result
    movie_id = movie_results[0].getID()
    print(movie_id) # Output: '0468569'    
    return movie_id
