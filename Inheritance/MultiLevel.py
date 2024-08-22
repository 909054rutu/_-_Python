class Team:
    def __init__(self,team_name):
        self.team_name=team_name


class Dev(Team):
    def __init__(self,team_name,role):
        super(). __init__(team_name)
        self.role=role

class Emp(Dev):
    def __init__(self,team_name,role,Emp_name):
        super(). __init__(team_name,role)
        self.Emp_name=Emp_name
    def display(Self):
        print("Team Name:",Self.team_name)
        print("Role:",Self.role)
        print("Name:",Self.Emp_name)


ob=Emp("Sowftware Developer","Engineer","swami")
ob.display()
    
