from surprise import Dataset
from surprise import Reader
from surprise import SVD, NMF, KNNBasic
from surprise import evaluate, print_perf

import os

file_path = os.path.expanduser('restaurant_ratings.txt')
reader = Reader(line_format='user item rating timestamp', sep='\t')
data = Dataset.load_from_file(file_path, reader=reader)

# Split data once to ensure same fold is compared across the board.
data.split(n_folds=3) 

# # Part 5
algo = SVD()
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)

# # Part 6
algo = SVD(biased=False)
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)

# # Part 7
algo = NMF()
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)

# # Part 8 
algo = KNNBasic(sim_options = {'user_based': True })
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)

# # Part 9
algo = KNNBasic(sim_options = {'user_based': False })
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)

# Part 14
## User-Based Flavors
print('User-Based MSD')
algo = KNNBasic(sim_options = {
    'name': 'MSD', 
    'user_based': True 
})
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)

print('User-Based Cosine')
algo = KNNBasic(sim_options = {
    'name': 'cosine', 
    'user_based': True 
})
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)

print('User-Based Pearson')
algo = KNNBasic(sim_options = {
    'name': 'pearson', 
    'user_based': True 
})
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)

# ## Item-Based Flavors
print('Item-Based MSD')
algo = KNNBasic(sim_options = {
    'name': 'MSD', 
    'user_based': False
})
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)

print('Item-based Cosine')
algo = KNNBasic(sim_options = {
    'name': 'cosine', 
    'user_based': False
})
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)

print('Item-based Pearson')
algo = KNNBasic(sim_options = {
    'name': 'pearson', 
    'user_based': False
})
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)

# Part 15
for i in range(1, 30):
    print("kNN: " + str(i) + " for User-Based collaborative filtering.")
    algo = KNNBasic(sim_options = {
        'name': 'MSD', 
        'user_based': True 
    })
    perf = evaluate(algo, data,measures=['RMSE'])
    print_perf(perf)

for i in range(1, 30):
    print("kNN: " + str(i) + " for Item-Based collaborative filtering.")
    algo = KNNBasic(sim_options = {
        'name': 'MSD', 
        'user_based': False
    })
    perf = evaluate(algo, data,measures=['RMSE'])
    print_perf(perf)