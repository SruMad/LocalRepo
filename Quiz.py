questions = ("where was Chhatrapati Shivaji Maharaj born?",
            "What was the name of Shivaji Maharaj's mother?",
            "In which year was Shivaji Maharaj crowned Chhatrapati?",
            " At which fort was Shivaji Maharaj's coronation held?",
            "Which was the first fort captured by Shivaji at the age of 16?")
options = (("A.RAIGAD", "B.PRATAPGAD","C.PANHALA","D.SHIVNERI"),
          ("A.SAIBAI","B.PUTALABAI", "C.JIJABAI", "SOYARABAI"),
          ("A.1665","B.1674","C.1680","D.1678"),
          ("A.SINHGAD", "B.RAIGAD", "C.TORNA", "D.PANHALA"),
          ("A.SINHGAD", "B.RAIGAD","C.PRATAPGAD","D.TORNA"))

answers =("A","C","B","B","D")
guesses =[]
score = 0
question_num= 0                         #its an index operator to operate index of options

for question in questions:
    print("****************************")
    print(question)
    for option in options [question_num]:
        print(option)

    guess = input("enter A , B, C, D----").upper() #if user type in lower use .upper() to default Upper
    guesses.append(guess)                          #append will add guesses in list to display in the end
    if guess == answers[question_num]:            
        score +=1
        print ("correct answer ! ")
    else:
        print ("Oops incorrect answer")
        print(f"{question_num} is the correct answer")

    question_num+=1

print ("-------*******--------")
print("---------RESULT---------")
print("------*********----------")

print("answer: " , end=" ")
for answer in answers:
    print(answer, end=" ")

print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions)*100)
print(f"----YOUR SCORE IS {score}----")

if score >= 80 :
    print ("You got in 1st class")
else :
    print ("You are an average")
