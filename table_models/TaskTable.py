class TaskTable:
    def __init__(self) -> None:
        self.taskId = None
        self.taskName = None
        self.projectName = None
        self.status = None
        self.startTimestamp = None
        self.completeTimestamp = None
        self.description = None

    def __str__(self) -> str:
        return f"[taskId: {self.taskId}, taskName: {self.taskName}, projectName: {self.projectName}, status: {self.status}, startTimestamp: {self.startTimestamp}, completeTimestamp: {self.completeTimestamp}, description: {self.description}]"
