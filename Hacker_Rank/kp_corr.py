# Enter your code here. Read input from STDIN. Print output to STDOUT
# with numpy ---------------------------
import numpy as np

phys_scores = [15,  12,  8,   8,   7,   7,   7,   6,   5,   3]
hist_scores = [10,  25,  17,  11,  13,  17,  20,  13,  9,   15]

phys_mean = np.mean(phys_scores)
hist_mean = np.mean(hist_scores)


std_phys = np.std(phys_scores)
print(std_phys)
std_hist = np.std(hist_scores)

std_xy = 0
i = 0
for score in phys_scores:
    std_xy += (score - phys_mean)*(hist_scores[i] - hist_mean)
    i += 1

covariance = std_xy/(len(phys_scores))

r = covariance/(std_phys*std_hist)
print(round(r,3))

# without numpy----------------------------------------
phys_scores = [15,  12,  8,   8,   7,   7,   7,   6,   5,   3]
hist_scores = [10,  25,  17,  11,  13,  17,  20,  13,  9,   15]

phys_mean = sum(phys_scores)/len(phys_scores)
hist_mean = sum(hist_scores)/len(hist_scores)

def get_std(scores, mean):
    std=0
    for score in scores:
        std += (score-mean)**2
    return (std/len(scores))**.5

std_phys = get_std(phys_scores, phys_mean)
print(std_phys)
std_hist = get_std(hist_scores, hist_mean)

std_xy = 0
i = 0
for score in phys_scores:
    std_xy += (score - phys_mean)*(hist_scores[i] - hist_mean)
    i += 1

covariance = std_xy/(len(phys_scores))

r = covariance/(std_phys*std_hist)
print(round(r,3))
