import pandas as pd
import random as rd
import matplotlib.pyplot as plt

#read raw hs300 data
hs300 = pd.read_excel("399300.xlsx")
#hs300 = pd.DataFrame(hs300)
print(hs300)

#select close price for compute
selected_hs300 = hs300.close

#set random sample mark
random_mark = list(range(len(selected_hs300)))

#set sample numbers and cycle mumbers
sample_num = 1000
cycle_num = 10000

#iniciate sample list and average list
sample = list(range(sample_num))
avg_sample = list(range(cycle_num))

#start main cycle
for n in range(cycle_num):
    #refresh random_mark
    rd.shuffle(random_mark)

    #print cycle number
    print("Cycle "+str(n))
    for i in range(sample_num):
        sample[i] = selected_hs300[random_mark[i]]

    #compute sample's average value for this cycle
    avg_sample[n] = sum(sample) / len(sample)

#print predict average value and real average value
print("Predict average: "+str(sum(avg_sample) / len(avg_sample)))
print("Real average: "+str(sum(selected_hs300) / len(selected_hs300)))

#set window size
plt.figure(dpi=128, figsize=(10,6))

#show hist plot
plt.hist(avg_sample, 100, color="Blue", density=1)
plt.show()