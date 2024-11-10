"""
Word Occurrences
Estimate: 120 minutes
Actual:   ?? minutes

This time is also counting the time it taken to complete the other project file
"""
import datetime


class ProjectManagement:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = cost_estimate
        self.completion_percentage = int(completion_percentage)

        self.converted_date = datetime.datetime.strptime(self.start_date, "%d/%m/%Y").date()


    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, estimate: {self.cost_estimate}, completion: {self.completion_percentage} %"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100
