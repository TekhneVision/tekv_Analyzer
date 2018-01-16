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

   
def createDataSetComparisonReport(dataSetId_A, dataSetId_B): # DataSet_A is the file to compare against.
    dataSetA = dataFileUtil.getFileData(dataSetId_A, 'file')
    dataSetB = dataFileUtil.getFileData(dataSetId_B, 'file')
    dataSets = [dataSetA, dataSetB]
    result = trainingA.compareDataSets(dataSets, 0)
    dataFileUtil.create_CSV_File(result[1], 'HR Comparison Report Missing Dates')
    

createNonCompliantMissingDatesReport('hrData')