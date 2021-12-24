from abc import ABC, abstractmethod
from models.DailyActivity import DailyActivity
from models.DayOverview import DayOverview


class DataRepository(ABC):
    @abstractmethod
    def commit():
        pass

    @abstractmethod
    def saveDailyActivity(self, dailyActivity: DailyActivity) -> DailyActivity:
        pass

    @abstractmethod
    def saveBulkDailyActivity(self, dailyActivityList: list) -> list:
        pass

    @abstractmethod
    def getTaskId(self, projectId: int, taskName: str) -> int:
        pass

    @abstractmethod
    def getProjectId(self, projectName: str) -> int:
        pass

    @abstractmethod
    def saveDayOverview(self, dayOverview: DayOverview) -> bool:
        pass

    @abstractmethod
    def getProjectInfo(self):
        pass

    @abstractmethod
    def getActiveProjects(self) -> list:
        pass

    @abstractmethod
    def getActiveTasksByProjectId(self, projectId: int) -> list:
        pass

    @abstractmethod
    def getTaskTypes(self) -> list:
        pass
