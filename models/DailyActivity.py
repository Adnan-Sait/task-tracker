import datetime

class DailyActivity:
    
    def __init__(self):
        """Instantiates the DailyActivity Object."""
        self.__date = None              # type: datetime.date
        self.__taskId = None            # type: int
        self.__type = None              # type: str
        self.__effort = None            # type: float
        self.__description = None       # type: str
    
    def getDate(self) -> datetime.date:
        return self.__date

    def setDate(self, date: datetime.date):
        self.__date = date

    def getTaskId(self) -> int:
        return self.__taskId

    def setTaskId(self, taskId: int):
        self.__taskId = taskId
    
    def getType(self) -> str:
        return self.__type
    
    def setType(self, type:str):
        self.__type = type
    
    def getEffort(self) -> float:
        return self.__effort
    
    def setEffort(self, effort: float):
        self.__effort = effort
    
    def getDescription(self) -> str:
        return self.__description
    
    def setDescription(self, description:str):
        self.__description = description

    def __str__(self):
        return f"[date: {self.__date}, taskId: {self.__taskId}, effort: {self.__effort}, description: {self.__description}]"