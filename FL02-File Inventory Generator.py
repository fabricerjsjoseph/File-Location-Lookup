#The purpose of this script is to display a hierachy like view of folders, subfolders and files that they contain
#Updated version of FL01

import glob
import pandas as pd
import re

def create_list(directory,inventory,sheetname):


    #This is a list comprehension where you are outputing the results in the for loop directly in the list
    files = [f for f in glob.glob(directory + '/**', recursive=True)]

    #Printing all objects in list in a readable format
    #for f in files :
        #print(f)




    #Creating a dataframe from list files
    df=pd.DataFrame(files)



    #Count no of '\' in each row and add values to new column called backslash count
    df['Backslash count']= df[0].str.count(r'\\',re.I)


    #printing df with backslash count
    #print(df)

    #Calculate max value in backslash count
    no_of_cols= df['Backslash count'].max()-1



    #CREATING NEW DATAFRAME
    #Spliting the string using \ as seperator
    df2= df[0].str.split('\\',n=no_of_cols,expand=True)

    #Creating column header list

    col_header= ['level '+str(i) for i in range(no_of_cols+1)]
    #print(col_header)

    #Renaming columns of df2
    df2.columns=col_header

    #print(df2)
    #Export df2 to csv
    #df2.to_csv("list.csv",index=False)
    #EXPORTING DATAFRAME TO EXCEL ( OVERRIDES EXISTING FILE EVERYTIME)
    #from pandas import ExcelWriter
    #writer=ExcelWriter('File Inventory.xlsx')
    #df2.to_excel(writer,'Other Learning File List',index=False)
    #writer.save()

    #EXPORTING DATA TO EXISTING EXCEL FILE
    from openpyxl import load_workbook

    #Loading the File Management Excel File
    #path='File Management Phase 1.xlsx'
    book=load_workbook(inventory)

    #Accessing pandas excel writer
    writer=pd.ExcelWriter(inventory,engine='openpyxl')
    writer.book = book

    #Final Step - Writing the dataframe to the Excel file loaded above
    df2.to_excel(writer,sheet_name=sheetname,index=False)

    #Saving and close the file
    writer.save()
    writer.close()

create_list(r'C:\Users\user\Documents\4.Other Learning','File Management Phase 1.xlsx','Other Learning Folder')