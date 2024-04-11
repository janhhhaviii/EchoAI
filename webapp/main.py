import streamlit as st
from PIL import Image
import speech_recognition as sr

def recognize_speech_from_file(audio_file):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # Record the entire audio file
        
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return "Could not request results from Google Speech Recognition service; {0}".format(e)

def page2():
    st.header("Speech Recognition from Audio File")
    st.write("Upload an audio file and let EchoAI convert speech to text.")
    
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav"])
    
    if uploaded_file is not None:
        recognized_text = recognize_speech_from_file(uploaded_file)
        st.write("Recognized text:", recognized_text)

def main():
    st.set_page_config(page_title="EchoAI", page_icon=Image.open("assets/logo.jpeg"))
    
    # Centering the image and reducing its size
    
    if st.session_state.page == "About":
        st.header("About EchoAI")
        col1, col2  = st.columns([1, 1])  # Create columns to adjust centering
        with col1:
            st.image('assets/image 1.jpeg', width=300, use_column_width=False)  # Adjust the width as needed
        with col2:
            st.write(" In many group discussions, especially in meetings or interviews, it can be challenging to keep track of who said what and to distill the key points from the conversation. This project addresses this challenge by providing an automated solution to summarize group conversations.It automatically summarize group conversations by identifying different speakers, segmenting the conversation, converting audio to text, and then using a Natural Language Processing (NLP) model to generate a summary.")
        if st.button("Go to Page 2"):
            st.session_state.page = "Page 2"

    elif st.session_state.page == "Page 2":
        page2()

if __name__ == "__main__":
    if "page" not in st.session_state:
        st.session_state.page = "About"
    main()
