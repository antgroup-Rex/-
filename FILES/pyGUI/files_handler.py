'''
files handling introduction functions
'''

import os

def get_file_details(full_file_name):
    fileNoExt,  file_extension = os.path.splitext(full_file_name)
    fileDetails = {}
    fileDetails['originalGivenName'] = full_file_name
    fileDetails['absPath']           = os.path.dirname(os.path.abspath(fileNoExt))        # 
    fileDetails['relPath']           = ''       # todo: find out how to get relative path
    fileDetails['basename']          = os.path.basename(fileNoExt)       # file name , with no extension
    fileDetails['extension']         = file_extension                    # '.txt' for example
    fileDetails['isFile']            = os.path.isfile(full_file_name)    # true if the given full name is existing file
    # print os.path.dirname(fileNoExt)
    # print os.path.curdir
    print fileDetails   # todo: how to print or set dict without sorting?
    print ('')
    
    return fileDetails


def sort_file_action_by_type(full_file_name):
    fileDict = get_file_details(full_file_name)
    if fileDict['extension'] == '.txt':
        # todo: ask to open as notepad and edit ?
        print "text file is given"
    elif fileDict['extension'] == '.py':
        # todo: ask to open as notepad and edit? , or execute and from which work folder?
        print "python file is given"
    elif fileDict['extension'] == '.csv':
        # todo: import data, and display on new list of loaded files and data records.
        print "csv data file is given"

    pass

if __name__ == '__main__':
    sort_file_action_by_type('..\pyGUI\perspectives.txt')
    sort_file_action_by_type('C:\Users\Ran_the_User\Documents\GitHub\pyFiles\FILES\pyGUI\perspectives.txt')
    '''
    print fileNoExt
    print file_extension
    print os.path.abspath(fileNoExt)
    print os.path.basename(fileNoExt)
    print os.path.dirname(fileNoExt)
    print os.path.isfile(fileNoExt)
    print os.path.isfile(full_file_name)
    print os.path.relpath(fileNoExt)
    print os.path.relpath(full_file_name)
    print os.path.curdir
    
    expected output:
    C:\Users\Ran_the_User\Documents\GitHub\pyFiles\FILES\pyGUI\perspectives
    .txt
    C:\Users\Ran_the_User\Documents\GitHub\pyFiles\FILES\pyGUI\perspectives
    perspectives
    C:\Users\Ran_the_User\Documents\GitHub\pyFiles\FILES\pyGUI
    False
    True
    perspectives
    perspectives.txt
    .

    '''
    # sort_file_action_by_type('JsonControlPanel.json')
    # sort_file_action_by_type('AUI_MAIN.py')
    # sort_file_action_by_type('perspectives.txt')