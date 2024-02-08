movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def imdb_check(movie):
   if movie["imdb"] > 5.5:
        return True
#2 
def sublist(dict):
    for i in range(len(dict)):
        if(imdb_check(dict[i]) == True):
            print(dict[i]["name"])
   
#3
def getbycategory(category):
    for i in range(len(movies)):
        if movies[i]["category"] == category:
            print(movies[i]["name"])

#4
def averageIMDB(lst):
    sum = 0
    for movie in lst:
        for i in range(len(movies)):
            if(movies[i]["name"] == movie):
                sum = sum + movies[i]["imdb"]

    av = sum / len(lst)
    return av

#5
def averageIMDBbycate(category):
    sum = 0
    cnt = 0
    for i in range(len(movies)):
        if movies[i]["category"] == category:
            cnt += 1
            sum = sum + movies[i]["imdb"]
    av = sum / cnt
    return av




# movie = input("Write the name of movie from dictionary: ")
movie = "We Two"
for i in range(len(movies)):
    if movies[i]["name"] == movie:
        print(imdb_check(movies[i]))
print("Movies with an IMDB score above 5.5: ")
sublist(movies)
# cate = input("Write the category you want to get: ")
cate = "Romance"
print("There is movies with category", cate, ":")
getbycategory(cate)
# lstmov = list(map(str, input("Write the movies: ").split(", ")))
lstmov = ["Hitman", "We Two", "Detective"]
print("The average is:", averageIMDB(lstmov))

# cateforav = input("Write th category: ")
cateforav = "Thriller"
print("Average imdb of movies which have category", cateforav, ":", averageIMDBbycate(cateforav))
