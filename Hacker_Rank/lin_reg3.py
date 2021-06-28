# %%
import numpy as np
from sklearn import linear_model
# from sklearn.linear_model import LinearRegression

phys_scores = [15,  12,  8,   8,   7,   7,   7,   6,   5,   3]
hist_scores = [10,  25,  17,  11,  13,  17,  20,  13,  9,   15]

x = np.array(phys_scores).reshape(-1,1)
y = np.array(hist_scores)

model = linear_model.LinearRegression()
model.fit(x,y)

print(model.coef_)
print(model.intercept_)

x_new = np.array([10]).reshape(-1,1)
# x_new = model.transform(x_new)
pred = model.predict(x_new)
print(round(*pred,1))


# %%
# plot the data and the best fit line
import matplotlib.pyplot as plt 
plt.scatter(x,y)
x2 = np.array(range(16)).reshape(-1,1)
y2 = model.predict(x2)
plt.plot(x2, y2)
plt.show()

# %%
# These scores don't look very correlated. Let's see what the 
# R value is
from scipy.stats.stats import pearsonr
r = pearsonr(phys_scores, hist_scores)
print('r = ', r[0])
print('2-tailed p-value = ', r[1])

# %%
import numpy
numpy.corrcoef(phys_scores, hist_scores)[0, 1]
