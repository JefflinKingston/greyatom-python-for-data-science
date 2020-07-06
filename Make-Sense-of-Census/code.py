# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census=np.concatenate([data,new_record])
print(data.shape)
print(census.shape)

age=np.array(census[:,0])
max_age=np.max(age)
min_age=np.min(age)
age_mean=round(np.mean(age),2)
age_std=round(np.std(age),2)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)

race_0=np.array(census[census[:,2]==0])
race_1=np.array(census[census[:,2]==1])
race_2=np.array(census[census[:,2]==2])
race_3=np.array(census[census[:,2]==3])
race_4=np.array(census[census[:,2]==4])

len_0=race_0.size
len_1=race_1.size
len_2=race_2.size
len_3=race_3.size
len_4=race_4.size

l=np.array([len_0,len_1,len_2,len_3,len_4])
m=l.min()
minority_race=list(l).index(m)
print(minority_race)

senior_citizens=np.array(census[census[:,0]>60])
working_hours_sum=senior_citizens[:,6].sum()
senior_citizens_len=senior_citizens.shape
avg_working_hours=round(working_hours_sum/senior_citizens_len[0],2)
print(working_hours_sum)
print(avg_working_hours)

high=np.array(census[census[:,1]>10])
low=np.array(census[census[:,1]<=10])
avg_pay_high=round(high[:,7].mean(),2)
avg_pay_low=round(low[:,7].mean(),2)
print(avg_pay_high)
print(avg_pay_low)









