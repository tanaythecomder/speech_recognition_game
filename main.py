import speech_recognition as sr
import pyttsx3 
import webbrowser as web 
import random  
import time


def saytext(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()



def recognizse_text_from_speech(recogniser, microphone):
    if not isinstance(recogniser, sr.Recognizer):
        raise TypeError("'recogniser' must be of Recognize type")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("'microphone' must be of Microphone type")
    response = {
        "success":True,
        "error":None,
        "Transcript":None
    }
    with microphone as source:
        
        recogniser.adjust_for_ambient_noise(source)
        print("Now Guess")
        audio = recogniser.listen(source)
        try:
            response["Transcript"] = recogniser.recognize_google(audio)
        except sr.RequestError:
            response["error"]="Api unavailable"
            response["success"]=False
        except sr.UnknownValueError:
            response["error"] = "Unable to recognise speech"
    return response
if __name__ == "__main__":
    words_to_be_guess = ["Facebook","Google","Microsoft","Tesla","Tata"]
    no_of_guesses = 3
    Prompt_no = 5
    recogniser = sr.Recognizer()
    microphone = sr.Microphone()

    result = random.choice(words_to_be_guess)

    instructions = (
        "Let's see will you able or not to guess what i am thinking now:\n"
        "{words}\n"
        "Hurry You are left with only {n} attempt\n".format(words = ", ".join(words_to_be_guess),n=no_of_guesses)
    )
    print(instructions)
    time.sleep(3)

def game():
    for i in range(no_of_guesses):
        for j in range(Prompt_no):
            print("Attempt {}".format(i+1))
            response = recognizse_text_from_speech(recogniser, microphone)
            if (response["Transcript"] or not response["success"]):
                break
            saytext("I didn't catch that! Please Repeat")
        if response["error"]:
            saytext("error:{error}".format(error = response["error"]))
            break
        saytext("You said:{guess}".format(guess=response["Transcript"]))

        if result==response["Transcript"]:
            saytext("Hurray! You win the game")
            break
        elif i==no_of_guesses-1:
            saytext("Sorry, You lose! I was thinking of {} ".format(result))
        else:
            saytext("Incorrect buddy! Try again")
    
cont ="yes"
while cont=="yes":
    game()
    with sr.Microphone() as source2:
        recogniser.adjust_for_ambient_noise(source2,duration=1)
        saytext("If you want to continue say, yes")
        audio2 = recogniser.listen(source2)
        try:
            
            cont = recogniser.recognize_google(audio2)
            cont = cont.lower()
        except:
            saytext("Since, No respond we are closing the game")
            break

            
    
    
    





