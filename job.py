class Job:
    def __init__(self, title, description, employer, location, salary, poster_name):
        self.title = title
        self.description = description
        self.employer = employer
        self.location = location
        self.salary = salary
        self.poster_name = poster_name

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_employer(self):
        return self.employer

    def get_location(self):
        return self.location

    def get_salary(self):
        return self.salary

    def get_poster_name(self):
        return self.poster_name
