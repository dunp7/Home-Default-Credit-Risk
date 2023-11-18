# This is a py file to create all function 
import matplotlib.pyplot as plt
import seaborn as sns

# Check null and remove all the columns have %null > 90%

def find_and_remove_null_cols(df): # input is a data frame
    cols_found = df.loc[:,(df.isnull().sum(axis = 0) / df.shape[0]) >= 0.9].columns
    ## -> we can remove this from the table
    return df.drop(columns=cols_found,axis= 0) # output is newdf that drop all %null >90% cols


# List all available values in numerical data
def check_value(df): # Input is a dataframe which contains only numerical data
    for i in df.columns:
        great0 = df[i][df[i] > 0].count()
        equal0 =  df[i][df[i] == 0].count()
        smal0 = df[i][df[i] < 0].count()
        nan_total = df[i].isnull().sum()
        other_value = df.shape[0] - great0 - smal0 - nan_total - equal0
        print(f'{i}  has     >0 {great0},  =0 {equal0}  ,   <0 {smal0},    nan: {nan_total},   other values: {other_value}')


# Drawl all the pie chart of the categorical columns:
def plot_piechart(df): # input is categorical dataframe
    col= df.columns
    fig, ax = plt.subplots(round(len(col)/4),4,figsize=(20,10))
    ite = 0 
    for i in range(0,round(len(col)/4)):
        for j in range(0,4):
            sizes = df[col[ite]].value_counts(normalize=True)
            ax[i][j].pie(sizes, autopct='%1.1f%%')
            ax[i][j].set_title(col[ite], color = 'red')
            ite +=1
    # Show the figure
    plt.show()
