class UniClass(object):

    def __init__(self, name: str, students : int):
        self.name = name
        self.students = students

    def __Str__(self):
        return "{} {}".format(self.name, self.students)
