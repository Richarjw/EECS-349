from ID3 import ID3, test, prune
from parse import parse
import numpy as np
import random
import matplotlib.pyplot as plt

inFile = "house_votes_84.data"
data = parse(inFile)

"""
Now you will try your learner on the house_votes_84.data, and plot learning curves.

Specifically, you should experiment under two settings: with pruning, and without pruning. 

Use training set sizes ranging between 10 and 300 examples. 
For each training size you choose, perform 100 random runs, 
for each run testing on all examples not used for training 
(see testPruningOnHouseData from unit_tests.py for one example of this). 
Plot the average accuracy of the 100 runs as one point on a learning curve 
(x-axis = number of training examples, y-axis = accuracy on test data). 
Connect the points to show one line representing accuracy with pruning, the other without. 
Include your plot in your pdf, and answer two questions:

In about a sentence, what is the general trend of both lines as training set size increases, 
and why does this make sense?
In about two sentences, how does the advantage of pruning change as the data set size increases? 
Does this make sense, and why or why not?
"""

x = []
trend_basic = []
trend_prune = []
for size in range(10,300,10):
    x.append(size)
    accuracy_b = []
    accuracy_p = []
    for i in range(100):
        random.shuffle(data)
        train_set = data[:size]
        test_set = data[size:]

        tree = ID3(train_set)
        accuracy_b.append(test(tree,test_set))
        tree_p = prune(tree,test_set)
        accuracy_p.append(test(tree_p,test_set))
    trend_basic.append(np.mean(accuracy_b))
    trend_prune.append(np.mean(accuracy_p))
    
fig, ax = plt.subplots()
ax.plot(x, trend_basic, color='blue', label='$Default$')
ax.plot(x, trend_prune, color='orange', label='$Pruned$')
ax.legend(loc='lower right')
ax.set_xlabel('Training Set Size')
ax.set_ylabel('Test Set Accuracy')
ax.set_title('Pruned vs Standard Tree Accuracy')