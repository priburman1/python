import speech_recognition as sr  
   
  
r = sr.Recognizer()  
with sr.Microphone() as source:  
   print("Please wait. Calibrating microphone...")  
    
   r.adjust_for_ambient_noise(source, duration=5)  
   print("Say something!")  
   audio = r.listen(source)  
   

try:  
   print("google thinks you said '" + r.recognize_google(audio) + "'")  
except sr.UnknownValueError:  
   print("google could not understand audio")  
except sr.RequestError as e:  
   print("google error; {0}".format(e))  


