#!/usr/bin/env python
# coding: utf-8

# ### Importing Libraries

# In[85]:


#Importing the libraries
import pandas as pdf
import matplotlib.pyplot as matplt


# ### Reading csv file

# In[86]:


#Reading the csv file dataset.
df=pdf.read_csv("https://fsadata.github.io/fsa-headcount/data/fsa-headcount-as-at-31-january-2018.csv")

#printing the size of the dataset
print("\nSize of the Dataset = ",df.shape)
df.head(10)

colour=['red','green','blue','yellow','pink','magenta','lightgreen','lightblue','cyan']
# ### Checking null value in all the column

# In[87]:


#checking null values in the dataset
df.isnull().sum()


# ### All columns name

# In[88]:


#printing all columns name
df.columns


# ### Details of the dataframe and its datatypes

# In[107]:


#complete information about the dataset
df.info()


# ### Dataframe description

# In[108]:


#describing the dataset using describe function
df.describe()


# ### Line plot of the FSA Employees different gender wise.

# In[105]:


#Defining the function for plotting the line graph which has multiple line.
def linePlot(datadf):
    #creating plot with the appropriate size
    datadf.plot(x='Grade',y=["HeadcountFemale","HeadcountMale"],kind='line',figsize=(15, 5))
    matplt.title("FSA Employees headcount",color='blue')    #Setting the title name of the graoh with the color
    matplt.xlabel("Employee Grade",color='blue')            #setting the label of the x-axis with the color
    matplt.ylabel("No of Employee",color='blue')            #setting the label of the y-axis with the color
    matplt.show()

#calling the linePlot function
linePlot(df)

#showing the plot



# ### Counting all the no of employee by the grade of the employee

# In[93]:


headcountTotal=df.groupby(['Grade']).size().reset_index().rename(columns={0:'GradeCount'})
headcountTotal


# In[94]:


#finding the unique grade of employee
FinalGrade = df.Grade.value_counts().index
FinalGrade


# In[95]:


#finding the no of employee by the grade wise
finalHeadcount = df.Grade.value_counts().values
finalHeadcount


# ### Stem chart for the total no of employee by its grade wise

# In[96]:


#defining the function stemplot for plotting the data with more intractive way
def stemplot(x,y,col):
    #creating the loop for the color change and plot line for all the groups.
    for i in range(len(colour)):
        matplt.stem(x[i], y[i],linefmt=col[i],markerfmt='D')

    matplt.title("FSA Employees headcount",color='red')  #Setting the title of the graphs
    matplt.xlabel("Employee Grade",color='blue')         #setting the x - label
    matplt.ylabel("No of Employee")                      #setting the y - label
    matplt.show()

#calling the stemplot function with the color
stemplot(FinalGrade,finalHeadcount,colour)


# ### Finding all the unique division and the total no of employee division wise.

# In[97]:


#Finding the unique division in the dataset
finalDivision = df.Division.value_counts().index
finalDivision


# In[98]:


#Finding the employee count from the different division
finalHeadcountDivision = df.Division.value_counts().values
finalHeadcountDivision


# ### Bar Plot of the employee data division wise

# In[99]:


#defining the barplotgraph function for plotting the data of the employee division wise.
def barplotgraph(x,y,col):
    #code for plotting the graph
    matplt.barh(x, y, linewidth=1, color=col)
    #setting the title of the graph
    matplt.title("Division wise Employee",color='red')
    #setting the x - label of the graph
    matplt.xlabel("No of Employee",color='blue')
    #setting the y - label of the graph
    matplt.ylabel("Name of Division")
    matplt.show()

#Calling the function for ploting the bar graph
barplotgraph(finalDivision,finalHeadcountDivision,colour)


# In[ ]:




