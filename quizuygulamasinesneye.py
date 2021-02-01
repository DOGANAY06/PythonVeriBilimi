#Question

class Question():
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer


class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0 #ilk skor 0 dır
        self.questionIndex=0  #ilk soru gelmesi için index 0 dan başlar

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self): #yukarıdaki classın bir örneği question classının
        question=self.getQuestion()
        print(f'Soru {self.questionIndex+1}:{question.text}')

        for q in question.choices: #secenekleri açtık
            print("-"+q)
        
        answer=input("Cevap:") #cevap girişini oluşturduk
        self.quess(answer) #soru kontrol fonksiyonuna yolluyoruz
    def quess(self,answer):
        question=self.getQuestion()
        if question.checkAnswer(answer):
            self.score +=1 #skoru artırmak için 

        self.questionIndex +=1 #1 sonraki soruya geçmek içi

    def loadQuestion(self): #döngü hazırladık gibi 
        if len(self.questions) ==self.questionIndex:
            self.showScore() #döngü aşarsak skore bilgisi gözükecek
        else:
            self.displayProgress()
            self.displayQuestion()
    def showScore(self):
        print("Skorunuz: ",self.score)
    def displayProgress(self):
        totalquestion=len(self.questions)
        QuestionNumber=self.questionIndex+1

        if QuestionNumber >=totalquestion:
            print("Quiz bitti")
        else:
            print(f"Question {QuestionNumber} of {totalquestion}".center(100,"*"))


q1=Question("En iyi programlama dili hangisidir  ?",["C#","C++","Java","Python"],"Python") #ilk text soru 2.text secimler 3.tex cevap   her birini ayrı ayrı tırnaklar içinde yazdık
q2=Question("En popüler programlama dili hangisidir  ?",["C#","C++","Java","Python"],"C++")
q3=Question("En çok kazandıran programlama dili hangisidir  ?",["C#","C++","Java","Python"],"Java")
q4=Question("En kötü programlama dili hangisidir  ?",["C#","C++","Java","C"],"C")
q5=Question("En çok kullanılan programlama dili hangisidir  ?",["C#","C++","Java","Python"],"Java")

questions=[q1,q2,q3,q4,q5]

quiz =Quiz(questions)



quiz.displayQuestion()

quiz.loadQuestion()

