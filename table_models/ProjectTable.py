class ProjectTable:
    def __init__(self) -> None:
        self.projectId = None
        self.projectName = None
        self.startTimestamp = None
        self.status = None
        self.description = None

    def __str__(self) -> str:
        return f"[projectId: {self.projectId}, projectName: {self.projectName}, startTimestamp: {self.startTimestamp}, status: {self.status}, description: {self.description}]"
