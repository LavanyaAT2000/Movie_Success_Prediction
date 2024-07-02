import imdb
ia = imdb.IMDb()

def getID(name):
    search = ia.search_person(name)  
    # loop for printing the name and id
    for i in range(len(search)):
        # getting the id
        id = search[i].personID
        # printing it
        return id
    
def image(id):
    try:
        code = id
        # getting person object
        actor = ia.get_person(code)
        # printing object it prints its name
        print(actor)
        # getting image
        image = actor['headshot']
        # printing the place
        return image
    except:
        return 'https://cdn-icons-png.flaticon.com/512/2815/2815428.png'





