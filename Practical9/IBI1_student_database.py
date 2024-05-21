class students: #create a class named students 
    def __init__(self,n,m,c,g,e):
        self.name=n
        self.major=m
        self.code_portifilo_score=c
        self.group_project_score=g
        self.exam_score=e
x=students('Jasonona','BMI',100,100,100)
print(x.name,x.major,x.code_portifilo_score,x.group_project_score,x.exam_score)