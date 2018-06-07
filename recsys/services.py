import tmdbsimple as tmdb
import random
import requests

API_KEY = 'a070e12e1c6d7b84ebc1b172c841a8bf'

def get_movie_by_id(movie_id):
    tmdb.API_KEY = API_KEY
    try:
        response = tmdb.Movies(movie_id).info()
        return response
    except:
        pass
    return


def exclude_seen(response,selected_items):
    new_response = []
    for movie in response:
        already_seen = False
        for movie_id in selected_items:
            if(movie["id"]==movie_id):
                already_seen = True
        if(already_seen==False):
            new_response.append(movie)
    return new_response

def top_rated(selected_items):
    tmdb.API_KEY = API_KEY
    movies = tmdb.Movies()
    response = movies.top_rated()
    response = exclude_seen(movies.results, selected_items)
    return response

def top_pop(selected_items, genres=False, crew=False, cast=False):
    tmdb.API_KEY = API_KEY
    genres_ids = []
    crew_ids = []
    cast_ids = []
    if(genres):
        for movie_id in selected_items:
            movie = tmdb.Movies(movie_id).info()
            for genre in movie["genres"]:
                genres_ids.append(genre["id"])
        #OR of genres
        genres_ids = '|'.join(str(x) for x in genres_ids)
        print("genres: " + genres_ids)
    if(crew):
        for movie_id in selected_items:
            credits = tmdb.Movies(movie_id).credits()
            for crew in credits["crew"][0:4]:
                crew_ids.append(crew["id"])
        #OR of crew
        crew_ids = '|'.join(str(x) for x in crew_ids)
        print("crew_ids: " + crew_ids)
    if(cast):
        for movie_id in selected_items:
            credits = tmdb.Movies(movie_id).credits()
            for cast in credits["cast"][0:4]:
                cast_ids.append(cast["id"])
        #OR of crew
        cast_ids = '|'.join(str(x) for x in cast_ids)
        print("cast_ids: " + cast_ids)

    discover = tmdb.Discover()
    response = discover.movie(
        with_genres=[genres_ids],
        with_crew=[crew_ids],
        with_cast=[cast_ids],
        sort_by='popularity.desc'
    )
    response = exclude_seen(discover.results, selected_items)
    return response

def get_random(selected_items, reclist_length, genres=False, crew=False, cast=False):
    tmdb.API_KEY = API_KEY

    genres_ids = []
    crew_ids = []
    cast_ids = []
    if(genres):
        for movie_id in selected_items:
            movie = tmdb.Movies(movie_id).info()
            for genre in movie["genres"]:
                genres_ids.append(genre["id"])
        #OR of genres
        genres_ids = '|'.join(str(x) for x in genres_ids)
        print("genres: " + genres_ids)
    if(crew):
        for movie_id in selected_items:
            credits = tmdb.Movies(movie_id).credits()
            for crew in credits["crew"][0:4]:
                crew_ids.append(crew["id"])
        #OR of crew
        crew_ids = '|'.join(str(x) for x in crew_ids)
        print("crew_ids: " + crew_ids)
    if(cast):
        for movie_id in selected_items:
            credits = tmdb.Movies(movie_id).credits()
            for cast in credits["cast"][0:4]:
                cast_ids.append(cast["id"])
        #OR of crew
        cast_ids = '|'.join(str(x) for x in cast_ids)
        print("cast_ids: " + cast_ids)


    discover = tmdb.Discover()
    response = discover.movie(
        with_genres=[genres_ids],
        with_crew=[crew_ids],
        with_cast=[cast_ids]
    )

    #this is due to a tmdb bug!!
    if(discover.total_pages > 1000):
        latest_page=1000
    else:
        latest_page=discover.total_pages
    if(discover.total_results<reclist_length):
        max_length=discover.total_results
    else:
        max_length=reclist_length

    movies = []
    count = 0
    while(count < max_length):
        random_page = random.randint(1,latest_page)
        response = discover.movie(
            with_genres=[genres_ids],
            with_crew=[crew_ids],
            with_cast=[cast_ids],
            page=random_page
        )
        random_movie = discover.results[random.randint(0,len(discover.results)-1)]
        already_selected=False
        for movie in movies:
            if(movie["id"]==random_movie["id"]):
                already_selected=True
        if(already_selected==False):
            movies.append(random_movie)
            count = count + 1


    movies = exclude_seen(movies, selected_items)

    while(len(movies)<reclist_length):
        random_movie = get_movie_by_id(random.randint(1,tmdb.Movies().latest()["id"]))
        if(random_movie!=None):
            already_selected=False
            for movie in movies:
                if(movie["id"]==random_movie["id"]):
                    already_selected=True
            if(already_selected==False):
                movies.append(random_movie)
        movies = exclude_seen(movies, selected_items)
    return movies

def recommend(selected_items, reclist_length):
    movies = top_pop(selected_items, genres=True, crew=False, cast=True)
    #movies = top_rated(selected_items)
    #movies = get_random(selected_items,reclist_length, genres=True, crew=False, cast=False)

    movies = movies[:reclist_length]
    return movies