"""
Docstring : this program is supposed to take input of 2 file names, compare their content 
and return yes if both contents are identical and return no if they are different 
with the differing lines.

#input
names of both files

#output
yes/no with the line of difference
"""


first = input('Enter the name of your first file')
firstFile = open(first)
second = input('Enter the name of your second file')
secondFile = open(second)
compareFiles(firstFile,secondFile)

def compareFiles(firstList,secondList):
    firstList = firstFile.readlines()
    secondList = secondFile.readlines()
    differenceList=[]
    for element in firstList:
        if element not in secondList:
            differenceList.append(element)
            return 'No', print(differenceList)
        else:
            return 'Yes'

