
import pyfiglet

print('\n')
print("Hello") 
playername = input ("What Is Your Name: ")
test = "Hello "+ playername;
#print(test + playername ) 
result = pyfiglet.figlet_format(test, font = ("bubble"))
print(result)
#print("hello  " + playername )  
mood = input ("How are you " + playername + "?" +'\n' )
#check the user input abd print response
if "good" in mood: print ("Iam good too")
elif "fine" in mood : print ("Iam fine too")
else: print ("its gonna be ok!\n")

answer = input("Should I tell you my name?\n") 
if "yes" in answer: 
    print ("my name is...")
    jayanth = pyfiglet.figlet_format("jayanth", font = ("bubble"))
    print (jayanth)

else: print("ok bye")