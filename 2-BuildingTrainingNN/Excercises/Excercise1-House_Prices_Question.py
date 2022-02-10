#!/usr/bin/env python
# coding: utf-8

# In this exercise you'll try to build a neural network that predicts the price of a house according to a simple formula.
# 
# So, imagine if house pricing was as easy as a house costs 50k + 50k per bedroom, so that a 1 bedroom house costs 100k, a 2 bedroom house costs 150k etc.
# 
# How would you create a neural network that learns this relationship so that it would predict a 7 bedroom house as costing close to 400k etc.
# 
# Hint: Your network might work better if you scale the house price down. You don't have to give the answer 400...it might be better to create something that predicts the number 4, and then your answer is in the 'hundreds of thousands' etc.

import tensorflow as tf
import numpy as np
from tensorflow import keras

# GRADED FUNCTION: house_model
def house_model(y_new):
    xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    ys = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5])
    # YOUR CODE SHOULD START HERE

    # YOUR CODE SHOULD END HERE
    
    return model.predict(y_new)[0]

prediction = house_model([7.0])
print(prediction)

# Expected Output: A number closed to 4.0
