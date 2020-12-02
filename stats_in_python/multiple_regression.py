# multiple regression

# %%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

URL = "http://www.stat.ufl.edu/~winner/data/pgalpga2008.dat"
df = pd.read_table(URL, delimiter=r"\s+", names=['avg_dist', 'accuracy', 'sex'])
df.describe()

# %%
# Now consider a multiple regression on the full data set,
# including both female and male golfers. Modify the third 
# variable to be a 0 if the golfer is female and 1 if the 
# golfer is male and fit the following regression:
# y* = b0 + b1*x1 + b2*X2
import statsmodels.formula.api as sfm
mod = sfm.ols(formula='accuracy ~ avg_dist + df.sex==2', data = df) # regress acc onto dist
res=mod.fit()
print(res.summary())

# %%
# PLOT
sns.set_style('darkgrid')
sns.scatterplot(x=df.avg_dist, y=df.accuracy, hue=df.sex)
plt.title('Percent on Fairway vs. Distance Hit')
plt.pot('x=')
plt.plot()

# %%
import statsmodels.api as sm
#define figure size
fig = plt.figure(figsize=(12,8))

#produce regression plots
fig = sm.graphics.plot_regress_exog(res, 'avg_dist', fig=fig)