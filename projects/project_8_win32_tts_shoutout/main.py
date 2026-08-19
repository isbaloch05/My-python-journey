
import win32com.client as  sp
names=["mark","john","sam","ismail"]
speak = sp.Dispatch("SAPI.SpVoice")
voices=speak.GetVoices()
for j in voices:
    print(j.GetDescription())
speak.Voice = voices[1]
for i in names:
    print(f"shoutout to : {i}")
    speak.Speak(f"shoutout to : {i}")

print(dir(sp))  # used for  checking the attributes and elements

# a=sp.Dispatch("SAPI.SpVoice")
# a.Speak("hi how are u")

