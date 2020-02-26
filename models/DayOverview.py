import datetime

class DayOverview:

    def __init__(self, dateRecorded, startTime, leavingTime, workHours,
                breakHours, lunchDuration, morningScheduleId, prayer):
        """Instantiates the DayOverview Object"""
        self.dateRecorded = dateRecorded              # type: datetime.date
        self.startTime = startTime                    # type: datetime.time
        self.leavingTime = leavingTime                # type: datetime.time
        self.workHours = workHours                    # type: float
        self.breakHours = breakHours                  # type: float
        self.lunchDuration = lunchDuration            # type: float
        self.morningScheduleId = morningScheduleId    # type: int
        self.prayer = prayer                          # type: boolean
    
    def __str__(self) -> str:
        return f"""[dateRecorded: {self.dateRecorded}, startTime: {self.startTime}, leavingTime: {self.leavingTime},
        workHours: {self.workHours}, breakHours: {self.breakHours}, lunchDuration: {self.lunchDuration},
        morningScheduleId: {self.morningScheduleId}, prayer: {self.prayer}]"""