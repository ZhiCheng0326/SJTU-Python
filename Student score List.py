class Class:
    def __init__(self):
        self.student_number = 0
        self.namelist = []
        self.allscore_list = []
        self.subjects = ["English", "Maths", "Physics", "Chemistry"]

    def addStudent(self,student_name,score_list):
        self.student_number += 1
        self.namelist.append(student_name)
        self.allscore_list.append(score_list)
        #print self.namelist,self.allscore_list

    def printStudent(self,student_name):
        for i in range(len(self.namelist)):
            if student_name == self.namelist[i]:
                print self.namelist[i]
                score_list = self.allscore_list[i]
                #print score_list
                j = 0
                k = 0
                while j in range(4):
                    print "%s is %.2d" % (self.subjects[j], score_list[k])
                    j += 1
                    k +=1
            else:
                return
        print
            
    def printCurriculumScore(self,name):
        for a in range(len(self.subjects)):
            if name == self.subjects[a]:
                totalScore = 0 
                for b in self.allscore_list:
                    totalScore += b[a]
        print "The total score for %s is %d" % (name,totalScore)
        

    def averageScoreByStudent(self,student_name):
        for i in range(len(self.namelist)):
            if student_name == self.namelist[i]:
                #print self.namelist[i]
                score_list = self.allscore_list[i]
                #print score_list
        total = 0
        for score in score_list:
            total += score
        #print total
        averageScore = total / 4.0
        print "The average score for %s is %.2f " % (student_name, averageScore)
        
    def averageScoreByCurriculum(self,curriculum_name):
        for a in range(len(self.subjects)):
            if curriculum_name == self.subjects[a]:
                totalScore = 0 
                for b in self.allscore_list:
                    totalScore += b[a]
                #print totalScore
        averageScore = totalScore /float(self.student_number)
        print "The avearage per %s is %.2f" % (curriculum_name,averageScore)
                                  
class_a = Class()
class_a.addStudent("Tom", [90, 85, 76, 92])
class_a.addStudent("Ali", [78,82,84,78])
class_a.addStudent("Jack", [82,94,77,89])
class_a.addStudent("Peter", [92, 87, 79, 91])
print
class_a.printStudent("Tom")
class_a.printStudent("Jack")
print
class_a.printCurriculumScore("Maths")
class_a.printCurriculumScore("Physics")
print
class_a.averageScoreByStudent("Ali")
class_a.averageScoreByStudent("Peter")
print
class_a.averageScoreByCurriculum("English")
class_a.averageScoreByCurriculum("Chemistry")

