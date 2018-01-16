'''
Created on Jan 15, 2018

@author: Jerime
'''

# Search for records with missing dates.
def identifyMissingDates(dataSet):       
    nonCompliant = []
    compliant = []
    
    for row in dataSet:
        year = row[4]
        if year == "":
            nonCompliant.append(row)
        else:
            compliant.append(row)
 
    result = [compliant, nonCompliant]# Returns a list of list (Compliant and nonCompliant)
    return result
    


def compareDataSets(dataSets, headerKey):# index of the column/header that will be compared.
    dataSetA = dataSets[0]
    dataSetB = dataSets[1]
    
    for rowA in dataSetA:
        for rowB in dataSetB:
            if rowA[headerKey] == rowB[headerKey]:
                print('TODO')
        
    
    
    