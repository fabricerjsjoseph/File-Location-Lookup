#The purpose of this script is to search a file within a defined list of folders

import glob
import pandas as pd
import itertools
import os

def generate_df():

    #Create a list of folder location to conduct search into
    path_list=[r'C:\Users\user\Music',r'C:\Users\user\Videos',r'C:\Users\user\Google Drive',r'C:\Users\user\OneDrive',
                 r'C:\Users\user\Dropbox',r'C:\Users\user\Downloads',r'C:\Users\user\Documents',r'C:\Users\user\Creative Cloud Files',
                 r'C:\Users\user\Box Sync',r'C:\Users\user\Google Drive',r'C:\Users\user\Desktop']

    folder_list=[os.path.basename(path) for path in path_list]

    #Creation of list of all files in path_list
    files_in_all=[]

    #Initialise empty DataFrame
    master_df=pd.DataFrame()

    # Each list to store links to files in each folder of path_list
    for index,path in enumerate(path_list):
        files_in_path = [f for f in glob.glob(path + '/**', recursive=True) if not os.path.isdir(f)]
        df=pd.DataFrame(files_in_path)
        df['Root Folder Name']=folder_list[index]
        master_df=master_df.append(df)

    master_df.columns=['File_Path','Root_Folder']

    return master_df.to_csv('FM02_File_Search_df.csv',index=False)

#execute function to update csv file
generate_df()
