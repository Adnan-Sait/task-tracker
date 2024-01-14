class Constants:

    TASK_ENUM = {"kt": "Knowledge_Transfer"}
    TASK_DATA_VALIDATION = "=OFFSET(\'Project-Task Mapping\'!$A$2:$BB$999, 0, MATCH($C2, projectNames, 0)-1, COUNTA(OFFSET(\'Project-Task Mapping\'!$A$2:$BB$999, 0, MATCH($C2, projectNames, 0)-1, 999, 1)), 1)"
