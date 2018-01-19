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
    # Data setup utilizing "net" file as master dataset
    masterDataset = dataFileUtil.getFileData(datasetIds[0], 'file')
    datasetB = dataFileUtil.getFileData(datasetIds[1], 'file')
    dataSets = [masterDataset, datasetB]  
    netComparisonReport = trainingA.compareDataSets(dataSets, compareKey, messageList[0])    
    netFilteredDataset = trainingA.filterComparisonReport(netComparisonReport, datasetB, compareKey)    
    netFilteredReport = netFilteredDataset[0]
    netNnameList = netFilteredDataset[1]
    
    netTotal = len(masterDataset)
    hrTotal = len(datasetB)
    
    # Generate report utilizing "net" file as master dataset
    dataFileUtil.create_CSV_File(netComparisonReport, 'net- Comparison Report')    
    dataFileUtil.create_CSV_File(netFilteredReport, 'net- Filtered Comparison Report')
    dataFileUtil.create_CSV_File(netNnameList, 'net- Names from Filtered Report')
   
    
    # Data setup utilizing "hr" file as master record
    hrMasterDataset = dataFileUtil.getFileData(datasetIds[1], 'file')
    hrDatasetB = dataFileUtil.getFileData(datasetIds[0], 'file')
    hrDataSets = [hrMasterDataset, hrDatasetB]     
    hrComparisonReport = trainingA.compareDataSets(hrDataSets, compareKey, messageList[1])    
    hrFilteredDataset = trainingA.filterComparisonReport(hrComparisonReport, hrDatasetB, compareKey)    
    hrFilteredReport = hrFilteredDataset[0]
    hrNameList = hrFilteredDataset[1]
    
    dataFileUtil.create_CSV_File(hrComparisonReport, 'hr- Comparison Report') 
    dataFileUtil.create_CSV_File(hrFilteredReport, 'hr- Filtered Comparison Report')
    dataFileUtil.create_CSV_File(hrNameList, 'hr- Names from Filtered Report')
    

    
    # Create quantitative netComparisonReport analysis. 
    metaDataReport = []
    metaDataReport.append(['"net" File Total', netTotal])
    metaDataReport.append(['"hr" File Total', hrTotal])
    metaDataReport.append(['"net" - "hr" = ', netTotal - hrTotal])
    metaDataReport.append(['"net" Comparison Report Results'])
    metaDataReport.append(['"net" Comparison Report Total', len(netComparisonReport), 'Found in "net" but not in "hr"'])
    metaDataReport.append(['"net" Filtered Comparison Report Total', len(netFilteredReport),'Found in "net" but not in "hr"'])
    metaDataReport.append(['"net" Names extracted From Filtered Comparison Report', len(netNnameList)])
    metaDataReport.append(['"hr" Comparison Report Results'])
    metaDataReport.append(['"hr" Comparison Report Total', len(hrComparisonReport), 'Found in "hr" but not in "net"'])
    metaDataReport.append(['"hr" Filtered Comparison Report Total', len(hrFilteredReport),'Found in "hr" but not in "net"'])
    metaDataReport.append(['"hr" Names extracted From Filtered Comparison Report', len(hrNameList)])
    
    
    siteCodes = trainingA.calculateTotalBySite(netFilteredReport)
    for k, v in siteCodes.items():
        metaDataReport.append([k, v])
        
    dataFileUtil.create_CSV_File(metaDataReport, 'Reports Metadata') 
           
           
        
   
datasetIds = ['adData', 'hrData']    
message = ['Not found in HR dataset', 'Not Found in AD dataset']
createDataSetComparisonReport(datasetIds, 0, message)