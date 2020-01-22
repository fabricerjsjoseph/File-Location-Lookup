#The purpose of this script is to search a file within a defined list of folders

import glob

#Create a list of folder location to conduct search into
search_list=[r'C:\Users\user\Music',r'C:\Users\user\Videos',r'C:\Users\user\Google Drive',r'C:\Users\user\OneDrive',
             r'C:\Users\user\Dropbox',r'C:\Users\user\Downloads',r'C:\Users\user\Documents',r'C:\Users\user\Creative Cloud Files',
             r'C:\Users\user\Box Sync']

#Creation of list of all files in search_list
files_in_all=[]

for path in search_list:
    files_in_path = [f for f in glob.glob(path + '/**', recursive=True)]
    files_in_all.append(files_in_path)

import itertools
merged_list=list(itertools.chain(*files_in_all))

import pandas as pd

#Creating a dataframe from list files
df=pd.DataFrame(merged_list)


#Configuring the display of dataframe in IDE
pd.set_option('display.max_colwidth',500)
pd.set_option('display.max_rows',500)

#Remaining 1st an only column of dataframe
df.columns=['File Location']
#Create an uppercase version of File Location column
df['FILE LOCATION']=df['File Location'].str.upper()
#Creating new column to show file extension
df['File Extension']= df['File Location'].str.extract('(\.\w\w\w\w?)',expand=True)

#This will export every path in the search list (include actual files and path to folders and subfolers
#df.to_csv('FL03-Complete DataFrame.csv')

#This should only remove entries that does not have a file extension
new_df=df.dropna()


#List of keywords to search
keywords=['flowstate','flow','flow state']

#Converting list into regex friendly strings
keywords_regex= '|'.join(keywords)

#searching for key words and converting strings to uppercase
search_filter= new_df.stack().str.contains(keywords_regex).any(level=0)
#print(search_filter)

#Display Search Results
search_results=new_df[search_filter]
print(search_results['File Location'])

#Export search results to csv
#output='Search Results For '+ word+'.csv'
#search_results.to_csv(output)