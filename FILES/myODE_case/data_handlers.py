"""
general functions to get data and filter or write to file or any other options
"""
################
# imports of Scientific libraries and others

import  numpy           as      np
from    numpy           import  sin       # for better later code readability
from    numpy           import  cos       # for better later code readability
from    math            import  sqrt
from    random          import  randint
import  pandas          as      pd

import csv
##################################

def simulation_data_to_csv(time_vetor, state_vecotr_records, output_file_name):
    '''
    :param time_vetor: ndarray type
    :param state_vecotr_records:ndarray type
    :param output_file_name: str type
    :return: -
    posssible ref : https://docs.python.org/3.4/library/csv.html
    '''
    # todo: use better numpy functions to get this done more straight forward
    file_data = np.array([0,0,0,0,0,0,0], dtype=np.float64)[np.newaxis]
    for ndx,state in enumerate(state_vecotr_records):
        tmp = np.array([], dtype=np.float64)
        tmp = np.append(tmp ,time_vetor[ndx])
        one_record = np.append(tmp ,state_vecotr_records[ndx])
        one_record = np.array(one_record)[np.newaxis]    #1D to 2D as [1,7] shaped
        #np,col_stack ?
        # one_record = np.column_stack((time_vetor[ndx], state))
        file_data = np.row_stack((file_data,one_record))
    with open(output_file_name, 'w') as csvfile:
        np.savetxt(csvfile, file_data, delimiter=",")
    pass

def read_data_from_csv_to_str_or_Numpy_list(input_file_name):
    '''

    :param input_file_name:
    :return: output is :
     raw as str
     data as list
     file_data as nparray
     np.array(data) as 2D nparray

     app ref : http://www.dyinglovegrape.com/data_analysis/part1/1da3.php
    '''
    file_data = np.array([0, 0, 0, 0, 0, 0, 0], dtype=np.float64)[np.newaxis]
    data=[]
    with open(input_file_name,'r') as csvfile:
        row_iterator = csv.reader(csvfile)#, delimiter=',', quotechar='|')
        for row in row_iterator:
            # print(', '.join(row))
            npArr = np.array(row)[np.newaxis]
            file_data = np.row_stack((file_data, npArr))
            data.append(row)
    HeaderLine = data[0]
    data.pop(0)

    return HeaderLine, data

def read_data_from_csv_to_pandas(input_file_name):
    df = pd.read_csv(input_file_name, sep=',', header=None, usecols=[2])
    print df.values

def print_data_table(Header, data_as_numpy_list):
    import pandas as pd

    Header.append("Difference")
    for i in range(len(data_as_numpy_list)):
        diff = float(data_as_numpy_list[i][2]) - float(data_as_numpy_list[i][1])
        data_as_numpy_list[i].append(diff)
    new_data_tbl= pd.DataFrame(data_as_numpy_list, columns=Header)
    # print "Total in 1910: %d" % (np.sum(data_as_numpy_list))
    # print "Average in 1910: %d" % (np.mean(data_as_numpy_list))
    # print "Standard Deviation in 1910: %d" % (np.std(data_as_numpy_list))

    print tmp

def pd_trial():
    # web ref as http://www.dyinglovegrape.com/data_analysis/part2/2da2.php
    import pandas as pd
    from pandas import Series, DataFrame

    #Series related
    data1 = Series([6, 77, 888, 9999])
    print data1.index
    data2 = Series([8, 9, 11], index=["Joe", "Jane", "John"])
    print data2["Joe"]

    data3 = Series([8, 9, 11], index=["Joe", "Joe", "John"])
    print data3["Joe"]

    data2 += 1

    print data2[data2 >= 10]  # conditioning the element (not the index!)

    tmp=np.random.rand(20)  #array of 20 random numbers
    data4 = Series(np.random.rand(20)) # or as a Series
    print data4[data4 <= 0.275]

    # DataFrame related
    # Once you know about the Series, the idea of the DataFrame is simple: in a Series, you construct one index for your elements; in a DataFrame, you construct two.
    # Usually, these two indices are represented by "column headers" and "row labels"

    data = {'school': ['Baxters', 'Racine'], 'test scores': [90, 96]}  #dict varialbe
    table = DataFrame(data, index=['School 1', 'School 2']) # put it into dataframe format
    print table

    data = {'name': ['James', 'Jane', 'John', 'Jake',
                     'Audrey'], 'sex': ['M', 'F', 'M', 'M', 'F']}
    table = DataFrame(data)
    print table

    # DataFrame Manipulation
    data = {'name': ['James', 'Jane', 'John', 'Jake', 'Audrey'],
            'sex': ['M', 'F', 'M', 'M', 'F'],
            'age': [16, 17, 18, 20, 15],
            'height': [77, 56, 66, 61, 50]}
    print data

    print DataFrame(data)  #keeps alphabetic order of the columns
    table = DataFrame(data, columns=['name', 'age', 'sex', 'height']) #keeps desired order of the columns
    print table

    print table['name'] #pick a column
    print table[['name', 'age']] # or a list of columns

    # index access is by .ix similar to numpy _ix

    print table.mean()

    print table['height'].mean()

if __name__=='__main__':
    print "running from main"

    # file_csv = "quad_sim.csv"
    # h,d=read_data_from_csv_to_str(file_csv)
    # print_data_table(h,d)

    pd_trial()
else:
    # print __name__
    pass