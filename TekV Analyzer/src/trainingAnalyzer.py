'''
Created on Jan 15, 2018

@author: Jerime
'''

import util


# Search for records with missing dates.
def identifyMissingDates(dataSet):       
    nonCompliant = []
    compliant = []
    
    for row in dataSet:
        year = row[5]
        if year == "":
            nonCompliant.append(row)
        else:
            compliant.append(row)
 
    result = [compliant, nonCompliant]# Returns a list of list (Compliant and nonCompliant)
    return result
    


def compareDataSets(datasets, comparatorValue, messageList):# index of the column/header that will be compared.
    masterDataset = datasets[0]
    masterMessage = messageList[0]
    datasetB = datasets[1]
    messageB = messageList[1]
    
    key = comparatorValue
    result = []
   
    # Compare masterDataset to datasetB   
    for rowA in masterDataset:
        matchFound = False
        for rowB in datasetB:
            if rowA[key] == rowB[key]:
                matchFound = True
        
        if not matchFound:
            rowA.append(masterMessage)
            result.append(rowA)
            
    # Compare datasetB to masterDataset        
    for rowB in datasetB:
        matchFound = False
        for rowA in masterDataset:
            if rowB[key] == rowA[key]:
                matchFound = True
        
        if not matchFound:
            rowB.append(messageB)
            result.append(rowB)        
     
    return result
            
        
    
    
    