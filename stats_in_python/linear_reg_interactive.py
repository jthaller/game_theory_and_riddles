# linear regression, interactive, based on exercise in Baysian statistics course,
# originally in R 

# %%
import os 
import pandas as pd
import random
%pylab inline

## CHALLENGER SHUTTLE DATA
# %%
# To print a dataframe nicely in jupyter you need to turn it into html
from IPython.display import display
url = 'http://www.randomservices.org/random/data/Challenger2.txt'
# T = Temperature
# I = units of damage from flight
# index = flight number of US Challenger 
df = pd.read_table(url)
display(df)

# %%
import seaborn as sns
temp = df.iloc[:,0] #select all rows, 0th column
damage = df.I
# plt.scatter(temp, damage)
sns.scatterplot(temp, damage)
plt.xlabel('Temperature'), plt.ylabel('Damage')
plt.title('Challenger Data')
plt.show()

# %%
# add fitted line to scatterplot
temp = df.iloc[:,0]
damage = df.I
sns.set_style('whitegrid') 
sns.regplot(data = df, x = "T", y = 'I')
plt.xlabel('Temperature'), plt.ylabel('Damage')
plt.title('Challenger Data')
plt.show()

# %%
# OLS Linear Regression in statsmodels. idk why it's wrong
import statsmodels.formula.api as sfm
mod = sfm.ols('I ~ T', data = df) # regress I onto T
res = mod.fit()
print(res.summary())

# %%
# OLS Linear Regression in SciPy
from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(temp,damage)
print(f"slope: {slope}\nintercept: {intercept}\nstd: {std_err}")

# %%
# 95% confidence interval of fitted line
from scipy.stats import t                                                                            
n = 22 # counts                                                                                        
p = 2 # variables                                                                                           
alpha = 0.05                                                                                    
upper_q = t.ppf(1 - alpha / 2, n - p - 1)
print(f"lower 95%: {slope - std_err*upper_q}")
print(f"upper 95%: {slope + std_err*upper_q}")
print("Both are <0, so we're pretty sure there is a negative " \
       "relation between temperature and damage. These are also the" \
       "same as the frequentist confidence intervals.")

#%%
# The challenger launch was 31 degrees. How much damage do you predict?
prediction = slope*31 + intercept
print(f"Predicted damage: {prediction}")
prediction - std_err*upper_q*sqrt(1 + 1/23 + ((31 - np.mean(temp))**2 /22/np.var(temp)))

## ALTERNATE WAYS TO SCRAPE DATA IF IT'S MORE MESSY

# %%
# Extract text data from URL
import requests
from bs4 import BeautifulSoup
url = 'http://www.randomservices.org/random/data/Challenger2.txt'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.get_text()
print(results)
# %%
# Alternate method to turn string into dataframe
import io
data = io.StringIO(results)
df = pd.read_csv(data, sep="\t")
# To print a dataframe nicely in jupyter you need to turn it into html
from IPython.display import display
display(df)


## Galton dataset
## Predicting height of children from heights of parents (inches)
# %%
# Import data to dataframe
URL = 'http://www.randomservices.org/random/data/Galton.txt'
df = pd.read_table(URL)
print(display(df.head()))
df.describe()

# %%
sns.scatterplot(x = df.Father, y=df.Height)
sns.scatterplot(x = df.Mother, y=df.Height, color='red')
sns.scatterplot((df.Mother + df.Father)/2, y = df.Height, color='green')
plt.legend(['Mother', 'Father', 'avg'], loc='upper left')
plt.xlabel('Person')
plt.title('Child Height vs Parent Height')
plt.plot()


# %%
from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(df.Father,df.Height)
print(f"Father\nslope: {slope}\nintercept: {intercept}\nstd: {std_err}\nr: {r_value}")
slope, intercept, r_value, p_value, std_err = stats.linregress(df.Mother,df.Height)
print(f"Mother\nslope: {slope}\nintercept: {intercept}\nstd: {std_err}\nr: {r_value}")
slope, intercept, r_value, p_value, std_err = stats.linregress((df.Father+df.Mother)/2,df.Height)
print(f"Mean\nslope: {slope}\nintercept: {intercept}\nstd: {std_err}\nr: {r_value}")
print("\nGreatest Correlation is with the mean height of parents")




#  %% 
## QUIZ
import pandas as pd
URL = 'http://users.stat.ufl.edu/~winner/data/pgalpga2008.dat'
df = pd.read_table(URL, delimiter=r"\s+", names = ['avg_drive', 'acc_fairway', 'sex'])
men = df[df['sex'] == 2]
women = df[df['sex'] == 1]
men.head()

# %%
# Q1: plotting
import seaborn as sns
sns.set_theme(style='darkgrid')
sns.scatterplot(x = men.avg_drive, y=men.acc_fairway, label = 'Men')
plt.title('Men vs. Women')
plt.xlabel('Avg Drive Dist')
plt.ylabel('Fairway Accuracy')
# plt.legend(['Men', 'Women'])
sns.scatterplot(x = women.avg_drive, y=women.acc_fairway, label = 'Women')
plt.plot()


# %%
# Q2: linear regression stats
from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(women.avg_drive, women.acc_fairway)
print(f"slope: {slope}\nintercept: {intercept}\nstd: {std_err}")

import statsmodels.formula.api as sfm
mod = sfm.ols('acc_fairway ~ avg_drive', data = women) # regress acc onto dist
res=mod.fit()
print(res.summary())


# %%
# Plot with fitted lines
slope, intercept, r_value, p_value, std_err = stats.linregress(men.avg_drive, men.acc_fairway)
sns.scatterplot(x = men.avg_drive, y=men.acc_fairway, label = 'Men')
plt.plot(men.avg_drive, intercept + slope*men.avg_drive, 'r')
plt.title('Men vs. Women')
plt.xlabel('Avg Drive Dist'), plt.ylabel('Fairway Accuracy')
slope, intercept, r_value, p_value, std_err = stats.linregress(women.avg_drive, women.acc_fairway)
sns.scatterplot(x = women.avg_drive, y=women.acc_fairway, label = 'Women')
sns.scatterplot(x=[260], y=[74.075], label='prediction', markers='x')
plt.plot(women.avg_drive, intercept + slope*women.avg_drive, 'b', label='fitted line women')
plt.plot()

# %%
# prediction. Q4
print(f"{slope}\n{intercept}")
def predict_woman(x):
       return slope*x + intercept
print(f"y={predict_woman(260)}")

# %%
# gives a 95% posterior predictive interval for 
# the driving accuracy of a new female golfer whose 
# average driving distance is x=260x=260 yards
# this didn't match with the quiz answer for some reason
from scipy import stats                                                                     
n = women.avg_drive.size # counts                                                                                        
p = 2 # variables
# p<0.05, 2-tail
# equivalent to Excel TINV(0.05,999)
t=stats.t.ppf(1-0.025, n-2)
print(f"t={t}")
xmean = np.mean(women.avg_drive)
sx = np.var(women.avg_drive, ddof=1) # sample variance of driving range
k = sqrt(1 + 1/n + ((260-xmean)**2)/((n-1)*sx**2))
print(f"lower 95%: {predict(260) - t*std_err*k}")
print(f"upper 95%: {predict(260) + t*std_err*k}")

# %%