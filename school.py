class School:
    def __init__(self, school, roster={}):
        self.school = school
        self.roster = roster
    def add_student(self, full_name=None, grade=None):
        self.full_name = full_name
        self.grade = grade
        self.roster.update({full_name : grade})
    def Grade(self, grade=int):
        self.grade = grade
        return self.roster[grade]
    def sort_roster(self):
        self.sort_roster = sort_roster
        return self.roster.items.sorted()
        

	



















		
		


	
	
	
	

	

