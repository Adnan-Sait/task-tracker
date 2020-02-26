from models.DailyActivity import DailyActivity
from config.DatabaseConfig import DatabaseConfig
from utilities.SQLQueries import SQLQueries
from models.DayOverview import DayOverview
from models.Project import Project
from models.Task import Task

connection = DatabaseConfig.getConnection()

def connect() -> bool:
    global connection
    connection = DatabaseConfig.getConnection()
    return True

def saveDailyActivity(dailyActivity: DailyActivity) -> DailyActivity:
    cursor = connection.cursor()
    cursor.execute(SQLQueries.DAILY_ACTIVITY_INSERT, [dailyActivity.getDate(), dailyActivity.getTaskId(),
    dailyActivity.getType(), dailyActivity.getEffort(), dailyActivity.getDescription()])
    # queryResult = cursor.fetchone()
    # if (queryResult):
    #     dailyActivityRecord = queryResult
    # else:
    #     raise Exception("insert operation failed")
    return True

def saveBulkDailyActivity(dailyActivityList: list) -> list:
    cursor = connection.cursor()
    # dailyActivityRecordList = []
    for dailyActivity in dailyActivityList:
        cursor.execute(SQLQueries.DAILY_ACTIVITY_INSERT, [dailyActivity.getDate(), dailyActivity.getTaskId(),
        dailyActivity.getType(), dailyActivity.getEffort(), dailyActivity.getDescription()])
        # queryResult = cursor.fetchone()
        # if (queryResult):
        #     dailyActivityRecord = queryResult
        # else:
        #     raise Exception("insert operation failed")
        # dailyActivityRecordList.append(dailyActivityRecord)
    return True

def getTaskId(projectId: int, taskName: str) -> int:
    taskId = None
    cursor = connection.cursor()
    cursor.execute(SQLQueries.TASK_ID_GET+" WHERE \"projectId\"=%s AND lower(\"taskName\")=%s;", [projectId, taskName.lower()])
    queryResult = cursor.fetchone()
    if (queryResult):
        taskId = queryResult[0]
    else:
        raise Exception(f"No task with projectId, {projectId} and taskName, {taskName}")
    return taskId

def getProjectId(projectName: str) -> int:
    cursor = connection.cursor()
    cursor.execute(SQLQueries.PROJECT_ID_GET+" WHERE lower(\"projectName\")=%s;", [projectName.lower()])
    queryResult = cursor.fetchone()
    if (queryResult):
        projectId = queryResult[0]
    else:
        raise Exception(f"No project with projectName, {projectName}")
    return projectId

def saveDayOverview(dayOverview: DayOverview) -> bool:
    """Saves the DayOverview object in the DB
    
    Arguments:
        dayOverview {DayOverview} -- [description]
    
    Returns:
        bool -- [description]
    """
#     print(dayOverview)
    cursor = connection.cursor()
    cursor.execute(SQLQueries.DAY_OVERVIEW_INSERT, [dayOverview.dateRecorded, dayOverview.startTime, dayOverview.leavingTime,
    dayOverview.workHours, dayOverview.breakHours, dayOverview.lunchDuration, dayOverview.prayer, dayOverview.morningScheduleId])
#     queryResult = cursor.fetchone()
#     if (queryResult):
#         dayOverviewRecord = cursor.fetchone()
#         print(dayOverviewRecord)
#         return dayOverviewRecord
    return True

def getProjectInfo():
    """Retrieve details of all projects including effort
    """
    cursor = connection.cursor()
    cursor.execute(SQLQueries.PROJECT_DETAILED_INFO_GET)
    queryResult = cursor.fetchall()
    return queryResult

def getActiveProjects() -> list:
    """Get active projects
    """
    cursor = connection.cursor()
    cursor.execute(SQLQueries.ACTIVE_PROJECT_GET)
    queryResult = cursor.fetchall()
    if (len(queryResult) == 0):
        return None
    projectList = []
    for project in queryResult:
        projectData = Project()
        projectData.projectId = project[0]
        projectData.projectName = project[1]
        projectList.append(projectData)
    return projectList

def getActiveTasksByProjectId(projectId: int) -> list:
    """Get active tasks by project ID
    
    Arguments:
        projectId {int} -- [description]
    """
    cursor = connection.cursor()
    cursor.execute(SQLQueries.ACTIVE_TASK_BY_PROJECTNAME_GET, [projectId, "active"])
    queryResult = cursor.fetchall()
    if (len(queryResult) == 0):
        return None
    taskList = []
    for task in queryResult:
        taskData = Task()
        taskData.taskName = task[0]
        taskList.append(taskData)
    return taskList

def getTaskTypes() -> list:
    """Get Task Types
    """
    cursor = connection.cursor()
    cursor.execute(SQLQueries.TASK_TYPE_GET)
    queryResult = cursor.fetchall()
    if (len(queryResult) == 0):
        return None
    taskTypesList = []
    for taskType in queryResult:
        taskTypesList.append(taskType[0])
    return taskTypesList

def commit():
    connection.commit()

def disconnect():
    DatabaseConfig.endConnection()
    return True