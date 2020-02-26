class Project:

    def __init__(self):
        self.projectId = None        # type: int
        self.projectName = None      # type: str
        self.taskList = None       # type: list[Task]

    def __str__(self):
        return f"[id: {self.projectId}, name: {self.projectName}, taskList: {self.taskList}]"