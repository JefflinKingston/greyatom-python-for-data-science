# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank=pd.DataFrame(bank_data)

categorical_var=bank_data.select_dtypes(include = 'object')
print(categorical_var)

numerical_var=bank_data.select_dtypes(include = 'number')
print(numerical_var)

#STEP 2
banks=bank.drop(['Loan_ID'],axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode().iloc[0]
banks.fillna(bank_mode, inplace=True)
print(banks.isnull().sum())

#STEP 3
avg_loan_amount=pd.pivot_table(data=banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount')
print(avg_loan_amount)

#STEP 4

loan_approved_se=banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)

loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)

percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]
print(round(percentage_se,2))

percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]
print (round(percentage_nse,2))

#STEP 5
loan_term=banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )

big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)

#STEP 6
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values=loan_groupby.agg([np.mean])
print(mean_values)



