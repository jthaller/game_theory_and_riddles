# with ski-kit learn and numpy ----------------------------------------------------------------------
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib

phys_scores = np.array([15,  12,  8,   8,   7,   7,   7,   6,   5,   3]).reshape(-1,1) # x
hist_scores = np.array([10,  25,  17,  11,  13,  17,  20,  13,  9,   15]) # y

model = LinearRegression()
model.fit(phys_scores, hist_scores)

print('intercept:', model.intercept_)
print('slope:', model.coef_)



## without any imports -------------------------------------------------------------------------------
phys_scores = [15,  12,  8,   8,   7,   7,   7,   6,   5,   3] # x
hist_scores = [10,  25,  17,  11,  13,  17,  20,  13,  9,   15] # y

coordinates = [(phys_scores[i], hist_scores[i]) for i in range(len(phys_scores))]
# print(coordinates)

def lin_model(x, m, b):
    return m*x + b

def gradient_descent(x, y, m=.3, b=13.0, alpha=.0001, num_iter = 1000):
    i=0
    loss_cache = [0,0,0]
    best_mb = (0,0)
    min_loss = 1e6
    while i<num_iter:
        N = len(phys_scores)
        m = m - alpha/N * sum([x*(lin_model(x, m, b) - y) for x,y in coordinates])
        b = b - alpha/N * sum([lin_model(x, m, b) - y for x,y in coordinates])
        loss = sum([(lin_model(x, m, b) - y)**2 for x,y in coordinates])
        loss_cache.append(loss)
        if loss < min_loss:
            best_mb = (m,b)
            min_loss = loss
        # if loss_cache[-4] < loss_cache[-3] < loss_cache[-2] < loss_cache[-1]:
        #     return best_mb, loss_cache
        else:
            i+=1
    return best_mb, min_loss

(slope, intercept), min_loss = gradient_descent(phys_scores, hist_scores)
print('intercept: ', intercept)
print('slope: ', slope)
print('min loss: ', min_loss)