import pyttsx3

engine = pyttsx3.init()

with open("t.txt", "r") as file:
    data = file.read()
    
          
engine.setProperty("rate", 120) # speed set krna
voices = engine.getProperty("voices") 
engine.setProperty("voice", voices[1].id) # femal voice ke liye 1

# text1 =''' Hello Sana, how are you?
#   Your Python project is coming along great.
#  Now I can speak more than one line.
#  Keep learning and keep coding!
#  '''
# engine.say(text1)

# user = input(f"Speak what you want: ")
#engine.say(user)


engine.say(data)
engine.runAndWait() 
