# This is a py file to create all function 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

palette = '#f4dce4'

def draw_corr(df):
    '''Draw a correlation in dataframe
    Input: numeric data'''
    if df.shape[1] >= 10:
        correlation_matrix = df.corr()
        fig,ax = plt.subplots(figsize=(10, 7))
        fig.set_facecolor(palette)
        ax.set_facecolor(palette)
        sns.heatmap(correlation_matrix, annot=True, cmap='twilight', fmt='.2f', 
                    mask = np.triu(np.ones_like(correlation_matrix,dtype=bool))
                    ,linewidths=0.5,ax= ax)
        ax.set_title('Correlation Matrix', weight= 'bold', size = 15)
        ax.tick_params(left = False,  bottom = False)
    else:
        pass

class Univariate_Analysis:
    '''This is a class for a dataframe with only one columns'''
    def __init__(self,df,col, num = True):
        '''num here is a flag that if the dataframe input is numeric or not'''
        self.df = df[col]
        self.col = col
        self.num = num
    def visualize(self, bins = 100):
        fig,(ax1,ax2) = plt.subplots(1,2,figsize = (20,8))
        fig.set_facecolor(palette)
        ax1.set_facecolor(palette)
        ax2.set_facecolor(palette)
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
            ax2.tick_params(right = False,left= False)
            ax2.spines[['left','top','bottom']].set_visible(False)
            ax2.spines['right'].set_color('grey')
            ax2.set_ylabel('')
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
    def __init__(self,df,col1,col2 = 'TARGET' ,num = True):
        '''Input is df that contains TARGET columns
        col1 : columns you want to analyze
        col2 : always is categorical, default is TARGET
        num: FLag if col1 is numeric'''
        self.df = df[[col1,col2]]
        self.col1 = col1
        self.col2 = col2
        self.num = num
    # NUMERIC COLUMNS
    def plothistogram(self, bins = 100):
        if self.num == True:
            fig,(ax1,ax2) = plt.subplots(1,2,figsize = (15,7))
            fig.set_facecolor(palette)
            ax1.set_facecolor(palette)
            ax2.set_facecolor(palette)
            sns.histplot(self.df[self.df['TARGET'] == 0][self.col1], bins= bins, kde=True, ax = ax1)
            ax1.spines[['left','right','top']].set_visible(False)
            ax1.spines['bottom'].set_color('grey')
            ax1.tick_params(left = False, bottom = False)
            ax1.set_yticklabels([])
            ax1.set_ylabel(self.col1, size = 15, weight = 'bold')
            ax1.set_title('NON_DEFAULT')

            sns.histplot(self.df[self.df['TARGET'] == 1][self.col1], bins= bins, kde=True, ax = ax2)
            ax2.spines[['left','right','top']].set_visible(False)
            ax2.spines['bottom'].set_color('grey')
            ax2.tick_params(left = False, bottom = False)
            ax2.set_yticklabels([])
            ax2.set_ylabel('')
            ax2.set_title('DEFAULT')
        else:
            return 'Your input is not numeric'
        
        
    # CATEGORICAL COLUMNS
    def countplot(self):
        '''Count Plot for Categorical only'''
        if self.num == True:
            return 'Your input is not categorical'
        else:
            fig,ax = plt.subplots(1,2,figsize = (15,7))
            fig.set_facecolor(palette)
            ax[0].set_facecolor(palette)
            ax[1].set_facecolor(palette)
            order = self.df[self.col1].value_counts().index
            if self.df[self.col1].nunique() < 4:
                sns.countplot(data = self.df[self.df['TARGET'] == 0], x = self.col1,dodge=True,ax = ax[0], palette='pastel',order=order)
                ax[0].spines[['left','right','top']].set_visible(False)
                ax[0].spines['bottom'].set_color('grey')
                ax[0].set_yticklabels([])
                ax[0].tick_params(left = False, bottom = False)
                ax[0].set_title('Target= 0')
                ax[0].set_xlabel('')
                ax[0].set_ylabel(self.col1, size = 15, weight = 'bold')
                sns.countplot(data = self.df[self.df['TARGET'] == 1], x = self.col1,dodge=True,ax = ax[1], palette='pastel',order=order)
                ax[1].spines[['left','right','top']].set_visible(False)
                ax[1].spines['bottom'].set_color('grey')
                ax[1].set_yticklabels([])
                ax[1].tick_params(left = False, bottom = False)
                ax[1].set_title('Target= 1')
                ax[1].set_xlabel('')
                ax[1].set_ylabel('')
            else: 
                sns.countplot(data=self.df[self.df['TARGET'] == 0], y=self.col1, dodge=True, ax=ax[0], palette='pastel',order=order)
                ax[0].spines[['top', 'bottom', 'right']].set_visible(False)
                ax[0].spines['left'].set_color('grey')
                ax[0].set_xticklabels([])
                ax[0].tick_params(left=False, bottom=False)
                ax[0].set_title('Target = 0')
                ax[0].set_ylabel(self.col1, size=15, weight='bold')
                ax[0].set_xlabel('')

                # Horizontal bar plot for Target=1
                sns.countplot(data=self.df[self.df['TARGET'] == 1], y=self.col1, dodge=True, ax=ax[1], palette='pastel',order=order)
                ax[1].spines[['top', 'bottom', 'right']].set_visible(False)
                ax[1].spines['left'].set_color('grey')
                ax[1].set_xticklabels([])
                ax[1].tick_params(left=False, bottom=False)
                ax[1].set_title('Target = 1')
                ax[1].set_ylabel('')
                ax[1].set_xlabel('')
    