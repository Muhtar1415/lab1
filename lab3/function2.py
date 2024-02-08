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

#task1
def score(movies):
    title=input("Enter the name of the movie: ")
    for i in movies:
        if i["name"]==title:
            if i["imdb"]>5.5:
                print("True")
            else:
                print("False")

score(movies)

#task2
def sublist(movies):
    result = []
    for movie in movies:
        if movie["imdb"]>5.5:
            result.append(movie["name"])
    print(result)
sublist(movies)

#task3
def categories(movies):
    film_category = input("Enter the category of the movie: ")
    result = []
    for movie in movies:
        if movie["category"]==film_category:
            result.append(movie["name"])
    print(result)

categories(movies)

#task4
def computes_average():
    sum = 0
    count = len(movies)
    for m in movies:
        sum += m['imdb']
    return sum/count

print(round(computes_average(), 2))

#task5
def category_computes_average(category):
    sum_category_movie = 0
    for m in movies:
        if m['category'] == category:
            sum_category_movie += m['imdb']
    return sum_category_movie/len(category_list(category))

print(category_computes_average('Romance'))