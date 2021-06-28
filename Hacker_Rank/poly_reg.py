# https://www.hackerrank.com/challenges/predicting-office-space-price/problem
# Hackerrank polynomial Regression code
# look this works, but I have no idea how hackerrank is giving you the data
# it's not giving you a file or a variable to read. So I didn't get points for solving
# it, but really, I did solve it.

# using a pandas dataframe and polyregression
# %%
import pandas as pd
df = pd.read_csv('input03.txt', delimiter = ' ', skiprows=(1), names=(['f1', 'f2','f3']))
df.tail()

# %%
import matplotlib.pyplot as plt
y = df['f3'][0:-6]
x = df['f1'][0:-6]
plt.scatter(x,y)

# %%
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn.model_selection import train_test_split

X = df.iloc[0:-5, 0:2].values
y = df.iloc[0:-5, 2].values
variables = X
results = y

poly = PolynomialFeatures(degree=3)
poly_variables = poly.fit_transform(variables)

poly_var_train, poly_var_test, res_train, res_test = train_test_split(poly_variables, results, test_size = 0.25, random_state = 4)

regression = linear_model.LinearRegression()

model = regression.fit(poly_variables, results)
model = regression.fit(poly_var_train, res_train)

score = model.score(poly_var_test, res_test)
print(model.coef_)

poly_unknowns = poly.fit_transform(df.iloc[-4:,0:2].values)
predictions = regression.predict(poly_unknowns)
# print(predictions.reshape(-1,1))
print(*predictions, sep='\n')



## Now streamline it with a pipeline ------------------------
