score=0
print("Welcome to the Dengue Diagnosis !")
print("Answer the following questions with 'yes' or 'no'")
print("Do you have a high fever?")
ans=input().lower()
if ans=="yes":
    score+=1
else:
    print("Next Question")
print("Are you experiencing severe headaches?")
ans=input().lower()
if ans=="yes":
    score+=1
else:
    print("Next Question")
print("Do you feel pain behind the eyes?")
ans=input().lower()
if ans=="yes":
    score+=1
else:
    print("Next Question")
print("Do you have joint or muscle pain?")
ans=input().lower()
if ans=="yes":
    score+=1
else:
    print("Next Question")
print("Have you noticed any skin rash?")
ans=input().lower()
if ans=="yes":
    score+=1
    print("you got 1 score")
else:
    print("Next Question")
print("Are you feeling nauseous or vomiting?")
ans=input().lower()
if ans=="yes":
    print("correct!")
    score+=1
else:
    print("Next Question")
print("Do you feel fatigued or weak??")
ans=input().lower()
if ans=="yes":
    score+=1
else:
    print("Next Question")
print(f"You have answered {score} 'yes' out of 7 symptoms")
if score>=6:
    print("High likelihood of dengue. Please consult a doctor immediately")
elif score>=4:
    print("Possible dengue symptoms. Medical advice recommended")
elif score>=2:
    print("Some symptoms present, but may not be dengue. Monitor your health")
else:
    print("Unlikely to be dengue, but always consult a doctor if you're unsure.")
