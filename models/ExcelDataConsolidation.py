import datetime

class ExcelDataConsolidation:

    def __init__(self):
        """Instantiates the ExcelDataConsolidation Object"""
        self.__dateRecorded = None          # type: datetime.date
        self.__startTime = None             # type: datetime.time
        self.__leavingTime = None           # type: datetime.time
        self.__projectDict = {}             # type: dict
        self.__workHours = 0                # type: float
        self.__breakHours = 0               # type: float
        self.__lunchDuration = None         # type: float
        self.__prayer = False               # type: bool
    
    def getDateRecorded(self) -> datetime.date:
        """Get recordedDate"""
        return self.__dateRecorded

    def setDateRecorded(self, dateRecorded:datetime.date):
        """Set DateRecorded"""
        self.__dateRecorded = dateRecorded
    
    def getStartTime(self) -> datetime.time:
        """Get startTime"""
        return self.__startTime
    
    def setStartTime(self, startTime:datetime.time):
        """Set startTime"""
        self.__startTime = startTime
    
    def getLeavingTime(self) -> datetime.time:
        """Get leavingTime"""
        return self.__leavingTime
    
    def setLeavingTime(self, leavingTime:datetime.time):
        """Set leavingTime"""
        self.__leavingTime = leavingTime

    def getProjectDict(self) -> dict:
        return self.__projectDict
    
    def setProjectDict(self, projectDict:dict):
        self.__projectDict = projectDict
    
    def getWorkHours(self) -> float:
        """Get Work Hours"""
        return self.__workHours
    
    def setWorkHours(self, workHours:float):
        """Set Work Hours"""
        self.__workHours = workHours
    
    def getBreakHours(self) -> float:
        """Get Break Hours"""
        return self.__breakHours
    
    def setBreakHours(self, breakHours:float):
        """Set Break Hours"""
        self.__breakHours = breakHours
    
    def getLunchDuration(self) -> float:
        """Get Lunch Duration"""
        return self.__lunchDuration
    
    def setLunchDuration(self, lunchDuration: float):
        """Set Lunch Duration"""
        self.__lunchDuration = lunchDuration
    
    def getPrayer(self) -> bool:
        """Get Prayer"""
        return self.__prayer
    
    def setPrayer(self, prayer:bool):
        """Set Prayer"""
        self.__prayer = prayer

    def __str__(self):
        return f"""[dateRecorded: {self.__dateRecorded}, startTime: {self.__startTime}, leavingTime: {self.__leavingTime},
        projectList: {self.__projectDict}, workHours: {self.__workHours}, breakHours: {self.__breakHours},
        lunchDuration: {self.__lunchDuration}, prayer: {self.__prayer}]"""
