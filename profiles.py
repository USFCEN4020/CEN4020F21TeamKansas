class Profiles:
    def __init__(self, user, title, major, university, biography, experience, education):
        self.user = user
        self.title = title
        self.major = major
        self.university = university
        self.biography = biography
        self.experience = experience
        self.education = education

    def get_user(self):
        return self.user

    def get_title(self):
        return self.title

    def get_major(self):
        return self.major

    def get_university(self):
        return self.university

    def get_biography(self):
        return self.biography

    def get_experience(self):
        return self.experience

    def get_education(self):
        return self.education
