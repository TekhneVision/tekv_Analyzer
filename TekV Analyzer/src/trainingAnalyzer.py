'''
Created on Jan 15, 2018

@author: Jerime
'''
import dataFileUtil
import util


# Identify individuals who have not taken training or have outdated training dates
def identifyMissedTraning(timeFrame, dataSetId):
    dataSet = dataFileUtil.getFileData(dataSetId, 'file')
    
    nonCompliant = []
    compliant = []
    
    for row in dataSet:
        year = row[4]
        if year == "":
            nonCompliant.append(row)
        else:
            compliant.append(row)
 
    result = [compliant, nonCompliant]
    return result
    




timeFrame = {
    'from':'01/01/2017',
    'to':'12/31/2017'
}

result = identifyMissedTraning(timeFrame, 'hrData')

util.printList(result[1])
