from datetime import date
import unittest
from models.DailyActivity import DailyActivity

from services.MasterWorkbookService import MasterWorkbookService

class MasterWorkbookServiceTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.masterWorkbookService = MasterWorkbookService("C:/Projects/Personal/task-tracker/test_files/MasterSheet.xlsx")
        self.activeProjects = self.masterWorkbookService.getActiveProjects()

    ##
    # Get Task ID method
    ##
    def testSuccessGetTaskId(self) -> None:
        taskId = self.masterWorkbookService.getTaskId(2, "Vue")
        self.assertEqual(taskId, 2)

    def testSuccessCaseSensitivityGetTaskId(self) -> None:
        taskId = self.masterWorkbookService.getTaskId(6, "task_tracker")
        self.assertEqual(taskId, 8)

    def testFailIncorrectProjectTaskMappingGetTaskId(self) -> None:
        self.assertRaises(Exception, self.masterWorkbookService.getTaskId, 2, "Plan_Tasks")

    ##
    # Get Project ID method
    ##
    def testSuccessGetProjectId(self) -> None:
        projectId = self.masterWorkbookService.getProjectId("Self_Tools")
        self.assertEqual(projectId, 6)

    def testSuccessCaseSensitivityGetProjectId(self) -> None:
        projectId = self.masterWorkbookService.getProjectId("store_lookup")
        self.assertEqual(projectId, 3)

    def testFailIncorrectProjectNameGetProjectId(self) -> None:
        self.assertRaises(Exception, self.masterWorkbookService.getProjectId, "InvalidProject")

    ##
    # Get Active Projects method
    ##
    def testCountGetActiveProjects(self) -> None:
        self.assertEqual(len(self.activeProjects), 5)

    def testProjectStatusGetActiveProjects(self) -> None:
        for project in self.activeProjects:
            if(project.status.lower() != "active"):
                self.assertEqual(project.status.lower(), "active")
        self.assertTrue(True)
    
    ##
    # Get Active Tasks by Project ID
    ##
    def testSuccessGetActiveTasksByProjectId(self) -> None:
        activeTasksList = self.masterWorkbookService.getActiveTasksByProjectId(1)
        self.assertEqual(len(activeTasksList), 3)

    def testSuccessNoActiveTasksGetActiveTasksByProjectId(self) -> None:
        activeTasksList = self.masterWorkbookService.getActiveTasksByProjectId(2)
        self.assertEqual(len(activeTasksList), 0)

    def testFailIncorrectProjectIdGetActiveTasksByProjectId(self) -> None:
        self.assertRaises(Exception, self.masterWorkbookService.getActiveTasksByProjectId, -1)

    ##
    # Get Task Types
    ##
    def testSuccessGetTaskTypes(self) -> None:
        taskTypesList = self.masterWorkbookService.getTaskTypes()
        self.assertEqual(len(taskTypesList), 8)

if __name__ == "__main__":
    unittest.main()