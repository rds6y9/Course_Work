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

# Part 5
algo = SVD()
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)

# Part 6
algo = SVD(biased=False)
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)

# Part 7
algo = NMF()
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)

# Part 8 
algo = KNNBasic(sim_options = {'user_based': True })
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)

# Part 9
algo = KNNBasic(sim_options = {'user_based': False })
perf = evaluate(algo, data,measures=['RMSE', 'MAE'])
print_perf(perf)