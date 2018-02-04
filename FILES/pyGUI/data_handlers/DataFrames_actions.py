# handle pandas dataframe objects relevant actions

import pandas as pd

########################################
# class DFactions(pd.DataFrame):
# todo: how to add those function to built in dataframe object ?  generator ?
def get_head(pd, lines=1):
    pass
def get_tail(pd, lines=1):
    pass
def get_only_head_and_tail(pd, lines=1):
    pass
def get_columns_by_name(pd,req_col=None):

    pass
def get_rows_by_index(pd,req_row=None):
    pass

##################################################

if __name__=='__main__':

    print " script name : "+ __name__

    # small data
    introDict = {"index": [1,2,3,4],
                 "stamData": ["ran", "child", 0, 3]}
    testDF = pd.DataFrame(introDict)
    print introDict
    print testDF

    #bigger data
    testDF = pd.read_csv('df_data_example.csv')

    print get_head(testDF)