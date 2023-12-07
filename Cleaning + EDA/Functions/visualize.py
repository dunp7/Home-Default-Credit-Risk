# This is a py file to create all function 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def draw_corr(df):
    '''Draw a correlation in dataframe
    Input: numeric data'''
    correlation_matrix = df.corr()
    plt.figure(figsize=(14, 7))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()

class Univariate_Analysis:
    '''This is a class for a dataframe with only one columns'''
    def __init__(self,df,col, num = True):
        '''num here is a flag that if the dataframe input is numeric or not'''
        self.df = df[col]
        self.col = col
        self.num = num
    def visualize(self, bins = 100):
        fig,(ax1,ax2) = plt.subplots(1,2,figsize = (20,8))
        if self.num == True:
            '''For numeric data'''
            sns.histplot(self.df, bins= bins, kde=True, ax = ax1)
            ax1.spines[['left','right','top']].set_visible(False)
            ax1.spines['bottom'].set_color('grey')
            ax1.tick_params(left = False, bottom = False)
            ax1.set_yticklabels([])
            ax1.set_ylabel(self.col, size = 15, weight = 'bold')
            sns.boxplot(data= self.df, ax = ax2)
            ax2.tick_params(axis='y', labelright=True, labelleft=False)
            ax2.tick_params(right = False)
            ax2.spines[['left','top','bottom']].set_visible(False)
            ax2.spines['right'].set_color('grey')
        else:
            '''For categorical data'''
            data = self.df.value_counts()
            ax1.pie(data, labels=data.index.to_list(), autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
            ax1.set_ylabel(self.col, size = 15, weight = 'bold')

            if data.shape[0] <= 2:
                ax2.bar(data.index.astype(str), data.values, color=sns.color_palette('pastel'))
                for p in ax2.patches:
                    x,y = p.get_xy()
                    width = p.get_width()
                    height = p.get_height()
                    ax2.annotate(xy = (x + width/2, height + 1), text = height, size = 15, weight = 'bold')
                ax2.spines[['left','right','top']].set_visible(False)
                ax2.spines['bottom'].set_color('grey')
                ax2.set_yticklabels([])
            else:
                ax2.barh(data.index.astype(str), data.values, color=sns.color_palette('pastel'))
                for p in ax2.patches:
                    x, y = p.get_xy()
                    width = p.get_width()
                    height = p.get_height()
                    ax2.annotate(xy=(width, y + height / 2),text=width, size = 15, weight = 'bold')
                
                ax2.spines[['bottom','right','top']].set_visible(False)
                ax2.spines['left'].set_color('grey')
                ax2.set_xticklabels([])

            ax2.tick_params(left = False,bottom = False)

class Bivariate_Analysis:
    ''' A class of plotting to gain insight with Target value'''
    def __init__(self,df,col1, num = True):
        '''Input is df with 2 columns
        num: FLag if col1 is numeric'''
        self.df = df[[col1,'TARGET']]
        self.col1 = col1
        self.col2 = 'TARGET'
        self.num = num
    