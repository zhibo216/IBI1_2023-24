class students: #create a class named students 
    def __init__(self,n,m,c,g,e):  # the short names
        if not (0 <=c<= 100):  
            raise ValueError("Code Portfolio Score must be out of 100")  
        if not (0 <=g<= 100):  
            raise ValueError("Group Project Score must be out of 100.")  
        if not (0 <=e<= 100):  
            raise ValueError("Exam Score must be out of 100.") 
        self.name=n
        self.major=m
        self.code_portfolio_score=c
        self.group_project_score=g
        self.exam_score=e
x=students('Jasonona','BMI',100,100,100)  #name,major,code_portfolio score,group_project score, exam score
print(x.name,x.major,x.code_portfolio_score,x.group_project_score,x.exam_score)
