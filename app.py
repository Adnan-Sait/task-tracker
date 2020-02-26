import yaml
from config.DatabaseConfig import DatabaseConfig

DatabaseConfig.initializeConnection()
import controllers.ExcelController as excelController

configurationValues = {}
# Load configuration values
with open("./resources/config.yml") as configFile:
    configurationValues = yaml.load(configFile, Loader=yaml.FullLoader)
 
try:
    fileNameList = excelController.getNameOfFilesToBeProcessed()
    for fileName in fileNameList:
        excelController.readDailyActivitySheet(fileName, configurationValues['excelConfiguration']['sheetNames'])
except Exception as e:
    print(e)
 
excelController.createTaskTrackerWorkbook()