import streamlit as st
import time
import random


sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "If clouds had souls it would never stop raining.",
    "Streamlit makes it easy to build web apps with Python.",
    "Seek success, but always be prepared for random cats.",
    "Just because the water is red doesn't mean you can't drink it.",
    "Small habits make a big difference"
]

def calculate_wpm(start_time, end_time, typed_text):
    words = len(typed_text.split())
    time_taken = (end_time - start_time) / 60  
    return words / time_taken if time_taken > 0 else 0

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    correct_words = sum(1 for o, t in zip(original_words, typed_words) if o == t)
    return (correct_words / len(original_words)) * 100 if original_words else 0


st.title("Typing Master - Speed Test")


if 'text' not in st.session_state:
    st.session_state.text = random.choice(sample_texts)

st.write("**Type the following text:**")
st.info(st.session_state.text)

typed_text = st.text_area("Start typing here:", "", height=150)

if 'start_time' not in st.session_state:
    st.session_state.start_time = None

if st.button("Submit"):
    if not st.session_state.start_time:
        st.session_state.start_time = time.time()
    
    end_time = time.time()
    wpm = calculate_wpm(st.session_state.start_time, end_time, typed_text)
    accuracy = calculate_accuracy(st.session_state.text, typed_text)
    
    st.success(f"Your typing speed: {wpm:.2f} WPM")
    st.success(f"Your accuracy: {accuracy:.2f}%")
    
  
    st.session_state.start_time = None

def next_sentence():
    st.session_state.text = random.choice(sample_texts)
    st.session_state.start_time = None

if st.button("Next"):
    next_sentence()
