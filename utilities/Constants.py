class Constants:

    TASK_ENUM = {"kt": "Knowledge_Transfer"}
    TASK_DATA_VALIDATION = "=OFFSET(\'Project-Task Mapping\'!$A$2:$BB$20, 0, MATCH($C2, projectNames, 0)-1, COUNTA(OFFSET(\'Project-Task Mapping\'!$A$2:$BB$20, 0, MATCH($C2, projectNames, 0)-1, 20, 1)), 1)"