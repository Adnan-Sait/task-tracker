class Task:

    def __init__(self):
        self.taskName = None
        self.effort = None
        self.description = None

    def __str__(self):
        return f"[name: {self.taskName}, effort: {self.effort}, description: {self.description}]"