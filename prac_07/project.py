PROJECT_COMPLETE_PERCENTAGE = 100


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
        start_date_string = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start_date_string}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.percent_complete}%")

    def __lt__(self, other):
        """Compare two Project instances based on priority"""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if a Project is complete."""
        return self.percent_complete >= PROJECT_COMPLETE_PERCENTAGE
