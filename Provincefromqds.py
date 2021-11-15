# this is the main script file that will do all the work
# lets start by adding the processing steps here, as comments. We will then fill in the code

#Install relevant softwares if any needs to be installed

#import the two spreadsheets into VSC(python)

#Compare the two spreadsheet according two QDS and add province (new field/column) where they have the same QDS
    #import files
#from numpy import left_shift
import pandas as pd
import numpy as np 

qds = pd.read_csv("UpdateProvinces\QDSProvinces.csv")
print(qds.head(5))
transloc_data = pd.read_csv("UpdateProvinces\TransvaalRecords_withLocality.csv")
print(transloc_data.head(5))

    #Function for comparing the two csv
def compare():
    transloc_data.rename(columns={'QDS':'COD'}, inplace=True)
    #print(transloc_data.head(5))
    df_join1 = pd.merge(transloc_data,qds[['COD', 'PROVINCE']], on = 'COD', how = 'left')
    df_join1.rename(columns={'COD':'QDS'}, inplace=True)
    #print(transloc_data.head(5))
    df_join1 = df_join1.replace(np.nan, '', regex=True)
    print(df_join1.head(5))
compare()

    #do a loop

    #province using QDS and town name
#Isolate single word city names and compare to city spreadsheet according to city names and add province in the field above

#Export to csv
#def df_join1.to_csv("Updated Povinces")