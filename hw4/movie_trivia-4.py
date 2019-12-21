"""
HW4: Movie Trivia

This homework deals with the following topics:
- Dictionaries
- Sets
- Databases using dictionaries (not too far from how they really work!)
- Test driven development (TDD)

In this HW, we will deal with representing movie data using dictionaries,
with the goal of answering some simple movie trivia questions. For example,
“what is the name of the movie that both Tom Hanks and Leonardo DiCaprio
acted in?”

We will use 2 dictionaries. The first corresponds to information about
an actor and all the movies that he/she has acted in.  The second
corresponds to information about the critics’ score and the audience
score from https://www.rottentomatoes.com/, about the movies.  

Given that information, we will then want to answer some typical movie
trivia questions.

"""

#Use these first 2 functions to create your 2 dictionaries
import csv
def create_actors_DB(actor_file):
    """
    Creates a dictionary keyed on actors from a text file.
    """
    #open the file
    f = open(actor_file)
    movieInfo = {}
    #set the loop
    for line in f:
        line = line.rstrip().lstrip()
        actorAndMovies = line.split(',')
        actor = actorAndMovies[0]
        movies = [x.lstrip().rstrip() for x in actorAndMovies[1:]]
        movieInfo[actor] = movies
    f.close()
    #return the value
    return movieInfo



def create_ratings_DB(ratings_file):
    """
    Makes a dictionary from the rotten tomatoes csv file.
    """
    
    scores_dict = {}
    #open the file
    with open(ratings_file, 'r', encoding = 'utf-8') as csvfile:
        reader = csv.reader(csvfile)
        reader.__next__()
        for row in reader:
            scores_dict[row[0]] = [row[1], row[2]]
    #return the value       
    return scores_dict

def insert_actor_info(actor, movies, actordb):
    
    """
    insert the actor information in the database
    """
    #determine the value if in the database
    if actor in actordb:
        actordb[actor].append(movies)#append the value
    else:
        actordb.update({ actor:movies})#append the key and value
    
def insert_rating(movie, ratings, ratingsdb):
    """
     insert the rating in the database
    """
    #determine the value if in the database
    if movie in ratingsdb:
        ratingsdb[movie].append(ratings)#append the value
    else:
        ratingsdb.update({ movie:ratings})#append the key and value
    
def select_where_actor_is(actor_name, actordb):
    """
    find the movies that the actor in
    """
    #set empty list
    movies=[]
    lista=list(actordb.keys())
    #set the loop
    for i in lista:
        #equals to the lower version
        if actor_name== i.lower():
            movies.extend(actordb.get(i))
    #return the value
    return movies
               
def select_where_movie_is(movie_name, actordb):
    """
    find the actor in the movie
    """
    #set empty list
    actor_name=[]
    lista=list(actordb.keys())#get the key as list
    #set the loop
    for i in lista:
        for value in actordb.get(i):
            if movie_name==value.lower():
                actor_name.append(i)
    #return the value
    return actor_name
            
                   
def select_where_rating_is(comparison, targeted_rating, is_critic, ratingsdb):
    """
    the function to set comparision for the rating database
    """
    #set empty list
    moviename=[]
    MovieName=[]
    #the comparision of each case
    if comparison=='>' and is_critic==True:
        for ele in ratingsdb.values():
            if int(ele[0])>targeted_rating:
                moviename.extend(select_where_movie_is(ele[0],ratingsdb))#reuse the function
        
        MovieName.extend(avoid_duplicate(moviename))
        #return the value
        return MovieName
    
    if comparison=='=' and is_critic==True:
         for ele in ratingsdb.values():
             if int(ele[0])==targeted_rating:
                 moviename.extend(select_where_movie_is(ele[0],ratingsdb))#reuse the function
         #avoid dupilicate       
         
         MovieName.extend(avoid_duplicate(moviename))
         return MovieName#return the value
        
    if comparison=='<' and is_critic==True:
        for ele in ratingsdb.values():
            if int(ele[0])<targeted_rating:
                moviename.extend(select_where_movie_is(ele[0],ratingsdb))#reuse the function
        #avoid dupilicate
        
        MovieName.extend(avoid_duplicate(moviename))
        return MovieName#return the value
    
    if comparison=='>' and is_critic==False:
         for ele in ratingsdb.values():
             if int(ele[1])>targeted_rating:
                 moviename.extend(select_where_movie_is(ele[1],ratingsdb))#reuse the function
         #avoid dupilicate       
         
         MovieName.extend(avoid_duplicate(moviename))
         return MovieName#return the value
    
    if comparison=='=' and is_critic==False:
        for ele in ratingsdb.values():
            if int(ele[1])==targeted_rating:
                moviename.extend(select_where_movie_is(ele[1],ratingsdb))#reuse the function
        #avoid dupilicate       
        
        MovieName.extend(avoid_duplicate(moviename))
        return MovieName#return the value

    if comparison=='<' and is_critic==False:
        for ele in ratingsdb.values():
            if int(ele[1])<targeted_rating:
                moviename.extend(select_where_movie_is(ele[1],ratingsdb))#reuse the function
        #avoid dupilicate        
        
        MovieName.extend(avoid_duplicate(moviename))
        return MovieName#return the value
    
    return MovieName#return the value
                        

def get_co_actors(actor_name, actor_db):
    """
    get the co-actor
    """
    #set empty list
    actors=[]
    actorslist=[]
    lista=[]
    lista.extend(select_where_actor_is(actor_name,actor_db))
    if lista!=None:
        for i in lista:
            actors.extend(select_where_movie_is(i.lower(),actor_db))#reuse the function
            if actor_name in actors:
                actors.remove(actor_name)          
    for x in actors:
        if x not in actorslist:
            actorslist.append(x)
            for ele in actorslist:
                if ele.lower()==actor_name:
                    actorslist.remove(ele)
    return actorslist#return the value
        

def get_common_movie(actor1, actor2, actor_db):
    """
    get the common movie by two actors
    """
    #set empty list
    movies=[]
    lista=[]
    listb=[]
    lista.extend(select_where_actor_is(actor1,actor_db))#reuse the function   
    listb.extend(select_where_actor_is(actor2,actor_db))#reuse the function
    
    if lista!=None and listb!=None:
        for x in lista:
            for y in listb:
                if x==y:
                    movies.append(x)
    return movies#return the value

    
    
def good_movies(ratingsdb):
    """
    find the good movies which both score larger than 85
    """
    #set empty list
    n=[]
    #reuse the function

    for ele in select_where_rating_is('>', 85, True, ratingsdb):
        for ele1 in select_where_rating_is('>', 85, False, ratingsdb):
            if ele==ele1:
                n.append(ele)

    for ele2 in select_where_rating_is('>', 85, True, ratingsdb):
        for ele3 in select_where_rating_is('=', 85, False, ratingsdb):
            if ele2==ele3:
                n.append(ele2)
            
    for ele4 in select_where_rating_is('=', 85, True, ratingsdb):
        for ele5 in select_where_rating_is('>', 85, False, ratingsdb):
            if ele4==ele5:
                n.append(ele4)
                
    for ele6 in select_where_rating_is('=', 85, True, ratingsdb):
        for ele7 in select_where_rating_is('=', 85, False, ratingsdb):
            if ele6==ele7:
                n.append(ele6)
    
    
    n_set=set(n)#convert to set
    return(n_set)#return the value
                          
    
def get_common_actors(movie1, movie2, actor_db):
    """
    get the common actors by two movie
    """
    #set empty list
    actorname=[]
    actornames=[]
    actorname.extend(select_where_movie_is(movie1,actor_db))#reuse the function
    actorname.extend(select_where_movie_is(movie2,actor_db))#reuse the function
    for ele1 in select_where_movie_is(movie1,actor_db):
        for ele2 in select_where_movie_is(movie2,actor_db):
            if ele1==ele2:
                actornames.append(ele1)
        
    return actornames#return the value
def avoid_duplicate(lista):
    """
    to avoid the duplicate value in list
    """
    #set an empty list
    listb=[]
    for ele in lista:
        if ele not in listb:
            listb.append(ele)
    #return the list
    return listb
    
   
def main():
    """
    the main function of the program
    """
    #the functions to create two dictionarys
    actor_DB = create_actors_DB('moviedata.txt')
    ratings_DB = create_ratings_DB('movieratings.csv')
    
    #print the menu to show the users
    print('welcome to the actor and movies system, please enter the numbers which in front of the options.')
    print("------------------------------")
    print("1. enter the actor to get his/her films\n")
    print("2. Find the co-actor\n")
    print("3. Find the common movies\n")
    print("4. Get the good movies!\n")
    print("5. Get the common actors!\n")
    print("6. enter the film to find actors\n")
    print("7. find the film by the score:\n")
    print("-------------------------------")
    #let the users to select
    option=int(input("please enter you option (enter -1 to exit ):"))
    #determine the input is right
    while option!=-1:
        while True:
          if ((option==1)|(option==2)|(option==3)|(option==4)|(option==5)|(option==6)|(option==7)|(option==-1)):
               break
          else:
               print("wrong input, please enter 1-7")
               option=int(input("please enter you option(enter -1 to exit):"))
        #the option condition of each option
        if option==-1:
            break
        if option==1:
            #the parameter which used in function
            actorname=input("please enter the actors name")
            movies=select_where_actor_is(actorname.lower(), actor_DB)#use the function to get the movie
            print("this is the movies of this actor:",movies)
            #if the data is not in database, show not present
            if movies==[]:
                print('no present')
            option=int(input("please enter you option (enter -1 to exit ):"))
        if option==2:
            #the parameter which used in function
            name_actor=str(input('enter the actor name:'))
            coactor=get_co_actors(name_actor.lower(),actor_DB)#use the function to get the actor
            print('the co-actor is :',coactor)
            #if the data is not in database, show not present
            if coactor==[]:
                print('no present')
            option=int(input("please enter you option (enter -1 to exit ):"))
        if option==3:
            #the parameter which used in function
            actor1=str(input("please enter the name of first actor:\n"))
            actor2=str(input("please enter the name of second actor:\n"))
            com_movies=get_common_movie(actor1.lower(),actor2.lower(),actor_DB)#use the function to get common movie
            print("this is the common movies of this two actors:", com_movies)
            #if the data is not in database, show not present
            if com_movies==[]:
                print('no present')
            option=int(input("please enter you option (enter -1 to exit ):"))
        if option==4:
            #the parameter which used in function
            print("the good movies in this season:")
            movies=good_movies(ratings_DB)
            print(movies)
            option=int(input("please enter you option (enter -1 to exit ):"))
        if option==5:
            #the parameter which used in function
            movie1=str(input("please enter the name of first movie:\n"))
            movie2=str(input("please enter the name of second movie:\n"))
            com_actors=get_common_actors(movie1.lower(),movie2.lower(),actor_DB)#use the function to get common actors
            print("this actor in both movies:", com_actors)
            #if the data is not in database, show not present
            if com_actors==[]:
                print('no present')
            option=int(input("please enter you option (enter -1 to exit ):"))
        if option==6:
            #the parameter which used in function
            moviename=input("please enter the film's name:")
            actors=select_where_movie_is(moviename.lower(), actor_DB)#use the function to get actors
            print("this is the actors:",actors)
            #if the data is not in database, show not present
            if actors==[]:
                print('no present')
            option=int(input("please enter you option (enter -1 to exit ):"))
        if option==7:
            #the parameter which used in function
            compare=input("please enter the cmpare symbol,<,=,>\n")
            #determine if the input is right
            while True:
                if((compare=='<')|(compare=='=')|(compare=='>')):
                    break
                else:
                    
                    compare=input("wrong input,please enter the cmpare symbol,<,=,>\n")
                    
                
            score=int(input("please enter the standard score:\n"))
            stat=int(input("please enter you choice between 1. critics score, 2.audience score"))
            #determine if the input is right
            while True:
                if ((stat==1)|(stat==2)):
                    break
                else:
                    stat=int(input("wrong input,please enter you choice between 1. critics score, 2.audience score"))
            if stat==1:
                col=True
            if stat==2:
                col=False   
            movies=select_where_rating_is(compare,score,col,ratings_DB)#use the function to get the movies
            print("the film of this standard:",movies)
            #if the data is not in database, show not present
            if movies==[]:
                print('no present')
            option=int(input("please enter you option (enter -1 to exit ):"))
            
            
        
#display the main                
if __name__ == '__main__':
    main()
