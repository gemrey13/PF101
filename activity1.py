class IT2A:
    def __init__(self, name, section, subject) -> None:
        self.attendance = 0
        self.name = name
        self.section = section
        self.subject = subject

    def present(self):
        self.attendance += 1
    
    def absent(self):
        self.attendance -= 1

    def total_grade(self):
        print(f'Student: {self.name} - Attendance Grade for teh subject of {self.subject} is {self.attendance + 80}')

