class School:
    def __init__(self, school=None):
        self.school = school
        self.roster = {}
    def add_student(self, full_name=None, grade=None):
        self.full_name = full_name
        self.grade = grade
        if grade in self.roster: 
            self.roster[grade].append(full_name)
        else:
            self.roster[grade] = [full_name]
    def Grade(self, grade):
        self.grade = grade
        return self.roster[grade]
    def sort_roster(self):
        for i in self.roster.keys():
            self.roster[i]=sorted(self.roster[i])
	



















		
		


	
	
	
	

	

