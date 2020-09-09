# %%

import pandas as pd
%pylab inline

df = pd.read_csv('trainingdata.txt', names=["time_charged","battery_life"])
df.head()
plt.scatter(df["time_charged"],df["battery_life"])
plt.xlabel("Time Charged")
plt.ylabel("Battery Life")

#%%
df["battery_life"].max()
df["battery_life"].between(0,8, inclusive=False)
df.query('7.9 <= battery_life < 8')

# you can see the intercept is 0 and the slope is 4. Anything after 4 hrs
# of charge gets 8 hours battery life


