import services.ExcelService as excelService

def getNameOfFilesToBeProcessed() -> list:
    """Returns the list of file names that conform to the following
    template 'mm-dd-yyyy.xlsx'
    
    Returns:
        list -- [description]
    """
    return excelService.getExcelFileNamesToBeProcessed()

def readDailyActivitySheet(fileName:str, sheetNames:list):
    """Reads data from the Daily Activity sheet and populates the
    corresponding tables in the Database
    
    Arguments:
        fileName {str} -- [description]
        sheetNames {list} -- [description]
    
    Raises:
        e: [description]
    """
    try:
        excelFile = excelService.getFile(fileName)
        taskSheetData = excelService.readDataFromSheet(excelFile, sheetNames[0])
        overviewSheetData = excelService.readDataFromSheet(excelFile, sheetNames[1], 4)
        dateRecorded = excelService.getDateRecordedFromFileName(fileName)
        taskDataConsolidated = excelService.consolidateSheetData(dateRecorded, taskSheetData)
        print(taskDataConsolidated)
        dailyActivityList = excelService.populateDailyActivityObject(taskDataConsolidated)
        dayOverview = excelService.populateDayOverview(taskDataConsolidated, overviewSheetData)
        excelService.saveDailyActivityListAndDayOverview(dailyActivityList, dayOverview)
        try:
            excelFile.close()
            excelService.deleteFile(fileName)
        except Exception as e:
            print("Unable to delete file,", fileName)
    except Exception as e:
        print("Error while processing file,", fileName)
        raise e

def createTaskTrackerWorkbook():
    """Creates the daily activity sheet using the 
    saved template
    """
    excelService.createTaskTrackerWorkbook()