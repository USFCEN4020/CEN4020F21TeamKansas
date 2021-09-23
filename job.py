class Job:
    def __init__(self, title, description, employer, location, salary, post_name):
        self.__title = title
        self.__description = description
        self.__employer = employer
        self.__location = location
        self.__salary = salary
        self.__post_name = post_name

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_employer(self):
        return self.__employer

    def get_location(self):
        return self.__location

    def get_salary(self):
        return self.__salary

    def get_post_name(self):
        return self.__post_name
