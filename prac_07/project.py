PROJECT_COMPLETE_PERCENTAGE = 100
DATE_FORMAT_STRING = "%d/%m/%Y"


class Project:
    """Represent a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        """Initialise a Project instance.

        name: string
        start_date: datetime
        priority = integer
        cost_estimate: float
        percent_complete: integer
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        """String to represent a Project instance."""
        start_date_string = self.start_date.strftime(DATE_FORMAT_STRING)
        return (f"{self.name}, start: {start_date_string}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.percent_complete}%")

    def __lt__(self, other):
        """Compare two Project instances based on priority"""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if a Project is complete."""
        return self.percent_complete >= PROJECT_COMPLETE_PERCENTAGE

    def starts_after_date(self, date):
        """Determine if a Project starts on or after a given date"""
        return self.start_date >= date
