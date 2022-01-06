import yaml
import time

import controllers.ExcelController as excelController

configurationValues = {}
# Load configuration values
with open("./resources/config.yml") as configFile:
    configurationValues = yaml.load(configFile, Loader=yaml.FullLoader)

if (configurationValues["useDatabase"]):
    from config.DatabaseConfig import DatabaseConfig
    DatabaseConfig.initializeConnection()
 
fileCount = 0
try:
    try:
        fileNameList = excelController.getNameOfFilesToBeProcessed()
        for fileName in fileNameList:
            excelController.readDailyActivitySheet(fileName, configurationValues['excelConfiguration']['sheetNames'])
            fileCount += 1
    except Exception as e:
        print(e)
    finally:
        print("# of Files Processed: ", fileCount)
    
    excelController.createTaskTrackerWorkbook()
    print("Created file")
except KeyboardInterrupt as e:
    print("Interrupted")