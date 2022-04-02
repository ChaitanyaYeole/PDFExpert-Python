import pyttsx3
def text_to_audio(pdf_text,save_path,save_name):
    
    # initialize Text-to-speech engine
    engine = pyttsx3.init()
    # convert this text to speech
    text = pdf_text
    voices = engine.getProperty("voices")
    #print(voices)
    engine.setProperty("rate", 150)
    engine.setProperty("voice", voices[1].id)
    #engine.say(text)
    engine.save_to_file(text, save_path+"/"+save_name+".mp3")
    # play the speech
    engine.runAndWait()
