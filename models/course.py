class Course:
    def __init__(self, crn, title, section, seats):
        self.crn = crn
        self.title = title
        self.section = section
        self.seats = seats

    def __repr__(self):
        return f'[{self.title}-{self.section} ({self.crn}) | {int(self.seats[1]) - int(self.seats[0])}/{self.seats[1]} WL: {int(self.seats[4]) - int(self.seats[3])}/{self.seats[4]}]'

    def __eq__(self, other):
        if isinstance(other, Course):
            return self.crn == other.crn
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__repr__())
