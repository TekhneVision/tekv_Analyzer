'''
Created on Jan 16, 2018

@author: jerime.cortes.dev
'''
import dataFileUtil
import trainingAnalyzer as trainingA


def createNonCompliantMissingDatesReport(dataSetId):
    dataSet = dataFileUtil.getFileData(dataSetId, 'file')
    result = trainingA.identifyMissingDates(dataSet)    
    dataFileUtil.create_CSV_File(result[1], 'Cyber Awareness Training Missing Dates') 

   
def createDataSetComparisonReport(datasetIds, compareKey, messageList): # DataSet_A is the file to compare against.
    masterDataset = dataFileUtil.getFileData(datasetIds[0], 'file')
    datasetB = dataFileUtil.getFileData(datasetIds[1], 'file')
    dataSets = [masterDataset, datasetB]
    result = trainingA.compareDataSets(dataSets, compareKey, messageList)
    dataFileUtil.create_CSV_File(result, 'Comparison Report')
 
 

datasetIds = ['adData', 'hrData']    
message = ['Not found in HR dataset', 'Not Found in AD dataset']
createDataSetComparisonReport(datasetIds, 0, message)