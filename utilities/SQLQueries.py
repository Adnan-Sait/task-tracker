class SQLQueries:
    DAILY_ACTIVITY_INSERT = """INSERT INTO \"DailyActivity\" (\"dateRecorded\", \"taskId\", \"taskType\", \"effort\", \"description\")
    VALUES(%s, %s, %s, %s, %s) RETURNING *;"""
    DAY_OVERVIEW_INSERT = """INSERT INTO \"DayOverview\" (\"dateRecorded\", \"startTime\", \"leavingTime\", \"workHours\",
    \"breakHours\", \"lunchDuration\", \"prayer\", \"morningScheduleId\") VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;"""
    PROJECT_ID_GET = """SELECT \"projectId\" FROM \"Project\""""
    TASK_ID_GET = """SELECT \"taskId\" FROM \"Task\""""
    PROJECT_DETAILED_INFO_GET = """select p.\"projectId\", p.\"projectName\", sum(da.effort), p.description as effort
                    from \"Project\" p Inner join \"Task\" t on p.\"projectId\" = t.\"projectId\"
                    inner join "DailyActivity" da on da."taskId" = t."taskId"
                    group by p."projectId", p."projectName", p.description order by p."projectId";"""
    ACTIVE_PROJECT_GET = """SELECT "projectId", "projectName" from "Project" where status=1 ORDER BY "projectName";"""
    ACTIVE_TASK_BY_PROJECTNAME_GET = """SELECT "taskName" from "Task" where "projectId"=%s and lower("status")=%s ORDER BY "taskName";"""
    TASK_TYPE_GET = """SELECT "taskTypeName" from "TaskType" ORDER BY "taskTypeName";"""