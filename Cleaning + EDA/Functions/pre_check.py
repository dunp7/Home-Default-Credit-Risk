# This is a py file to create all function to pre check all the data
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import seaborn as sns


class pre_check_tool:
    def __init__(self,df):
        self.df = df
        self.numdf = None
        self.catdf = None
    def split_data(self):
        '''Func: split data into cate and num data'''
        self.numdf = self.df._get_numeric_data()
        for i in self.numdf.columns:
            if self.numdf[i].nunique() <= 3:
                self.numdf = self.numdf.drop(columns = i)

        self.catdf = self.df[[col for col in self.df if col not in self.numdf.columns]]
        

    # Check null
    def check_per_null(self):
        ''' Output is a dataframe showing the percent null in each column'''
        number_missing = self.df.isnull().sum()
        percent_missing = self.df.isnull().sum() * 100 / len(self.df)
        missing_value_df = pd.DataFrame({'number_missing' : number_missing,
                                        'percent_missing': percent_missing})
        return missing_value_df


    def find_null_cols(self,threshhold):
        '''Check null and remove all the columns have %null > threshhold(0< threshold < 1)
        Output : cols need to ve dropped
        '''
        cols_found = self.df.loc[:,(self.df.isnull().sum(axis = 0) / self.df.shape[0]) >= threshhold].columns
        return cols_found


    # List all available values in numerical and categorical data
    def check_value_num(self):
        '''List all the available values in numerical data'''
        for i in self.numdf.columns:
            great0 = self.numdf[i][self.numdf[i] > 0].count()
            equal0 =  self.numdf[i][self.numdf[i] == 0].count()
            smal0 = self.numdf[i][self.numdf[i] < 0].count()
            nan_total = self.numdf[i].isnull().sum()
            other_value = self.numdf.shape[0] - great0 - smal0 - nan_total - equal0
            print(f'{i}  has     >0 {great0},  =0 {equal0}  ,   <0 {smal0},    nan: {nan_total},   other values: {other_value}')

    def check_value_cat(self):
        '''List all the available values in categorical data'''
        for col in self.catdf.columns:
            print(f'col {col} : {list(self.catdf[col].unique())}\n')


    # check distribution 
    def dist_numchart(self):
        '''Drawl all the pie chart of the numeric columns'''
        for column in self.numdf.columns:
            sns.histplot(x=self.numdf[column])
            plt.title(f'Histogram for {column}')
            plt.show()

    def dist_catchart(self):
        '''Drawl all the pie chart of the categorical columns'''
        if not self.catdf.empty: 
            col= self.catdf.columns
            fig, ax = plt.subplots(round(len(col)/4),4,figsize=(20,10))
            ite = 0 
            for i in range(0,round(len(col)/4)):
                for j in range(0,4):
                    sizes = self.catdf[col[ite]].value_counts(normalize=True)
                    ax[i][j].pie(sizes, autopct='%1.1f%%')
                    ax[i][j].set_title(col[ite], color = 'red')
                    ite +=1
            # Show the figure
            plt.show()
        else:
            return 'Categorical DF is not available'

    def show_outliers(self):
        '''Input is numerical col in data frame
        Output : show outliers '''
        plt.figure(figsize=(6, 7))
        for column in self.numdf.columns:
            sns.boxplot(x=self.numdf[column])
            plt.title(f'Boxplot for {column}')
            plt.show()