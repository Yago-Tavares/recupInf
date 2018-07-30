import io
import operator
from surprise import Dataset
from surprise import KNNWithMeans,accuracy
from surprise.model_selection import train_test_split

__all__ = ['top5Movies', 'top3Neighbors', 'printRMSE']

movies = dict()
data_movies = io.open('ml-100k/u.item',encoding="ISO-8859-1").read().split('\n')
for i in data_movies:
    info = i.split('|')
    if(info != ['']): 
        movie_id = (info[0])
        movie_name = (info[1])
        movies[movie_id]=[movie_name]

movies_watched = dict()
data_users = io.open('ml-100k/u.data',encoding="ISO-8859-1").read().split('\n')
for i in data_users:
    info = i.split('\t')
    if(info != ['']):
        userID = info[0]
        movieID = info[1]
        if(userID in movies_watched):
            movies_watched[int(userID)].append(int(movieID))
        else:
            movies_watched[int(userID)] = [int(movieID)]

indications = dict()
moviesIds = set(movies.keys())
for i in movies_watched:
    moviesUserWatched= set(movies_watched[i])
    indications[i] = moviesIds.difference(moviesUserWatched)


data = Dataset.load_builtin('ml-100k')
trainset,testset = train_test_split(data,test_size =.2)

algo = KNNWithMeans(k=4, sim_options={'name': 'cosine', 'user_based': True})

algo.fit(trainset)
predictions = algo.test(testset)
rmse = accuracy.rmse(predictions,verbose = False)

def top5Movies(userId):
    indicationsByRating = dict()
    indicationsByUser = list(indications[userId])

    for i in indicationsByUser:
        indicationsByRating[i] = algo.predict(uid=str(userId),iid=str(i)).est
    indicationsByRating = sorted(indicationsByRating.items(), key=lambda x: x[1],reverse = True)
    top5 = indicationsByRating[:5]
    for w in top5:
        print(movies[w[0]],w[1])
    return top5

def top3Neighbors(uid):
    neighbors = algo.get_neighbors(iid=uid, k=3)
    print('3 users neighbors of user id 360: ' + str(neighbors))
    return neighbors

def printRMSE():
    return 'KNN RMSE: %.3f' % rmse
