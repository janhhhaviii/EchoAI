import streamlit as st
import speech_recognition as sr
def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        st.info("Listening... Speak something.")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        st.error("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")

def page2():
    st.title("Echo.AI")
    st.write("This app listens to your voice and transcribes it into text.")
    
    if st.button("Start Recording"):
        recognized_text = recognize_speech()
        if recognized_text:
            st.success("Recognition Complete!")
            st.write("Recognized text:", recognized_text)
