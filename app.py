import streamlit as st
import GetRessponceAi as testmine
import GetRelativePath as grp
import time
import SpeechRecognition as sr
from streamlit_option_menu import option_menu


def WriteState(state):
    with open(grp.resource_path('db\\key\\state.txt'), 'w') as file:
        file.write(state)
def ReadState():
    with open(grp.resource_path("db\\key\\state.txt"), 'r') as file:
        state = file.read()
    return state

def refresh_page(state):
    if ReadState() != state:
        WriteState(state)
        st.session_state.messages = [{"role":"assistant", "content" : "How Can I Help You"},]
    WriteState(state)
    

def WritePath(filepath):
    with open(grp.resource_path('db\\key\\path.txt'), 'w') as file:
        file.write(filepath)
def ReadPath():
    with open(grp.resource_path("db\\key\\path.txt"), 'r') as file:
        file_path = file.read()
    return file_path

def get_responce(user_input,this_file):
    return testmine.GetAnswer(user_input, this_file)

def VoiceChat():
    Chat(sr.Recognize())


st.set_page_config(page_title="Aimers - Learn WIth Us", page_icon="🤖")
st.title("Aimers - Learn With Us")

with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=["News","Education","Health","WomenHealth","Farming"],
        icons=["browser-safari","book-fill","heart-pulse-fill","person-standing-dress","flower3"],
        default_index=0,
    )
    #News = st.sidebar.button("News")
    #Faraming = st.sidebar.button("Farming")
    #Education = st.sidebar.button("Education")
    #Health = st.sidebar.button("Health")
    #WomenHealth = st.sidebar.button("Women Health")
    

voiceChat = st.sidebar.button("Voice Chat")
def type_message(message):
    msg_placeholder = st.empty()
    text = ""
    for char in message:
        text += char
        msg_placeholder.markdown(text)
        time.sleep(0.03) 
    

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"assistant", "content" : "How Can I Help You"},]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def Chat(ques):
    with st.chat_message("user"):
        st.markdown(ques)
    
    st.session_state.messages.append({"role":"user", "content" : ques})
    full_response = get_responce(ques, ReadPath())

    with st.chat_message("assistant"):
        
        type_message(full_response)
        st.session_state.messages.append({"role":"assistant", "content" : full_response})


if selected == "News":
    refresh_page("news")
    WritePath(grp.resource_path("db\\pdf\\news.pdf"))
if selected == "Farming":
    refresh_page("farming")
    WritePath(grp.resource_path("db\\pdf\\farming.pdf"))
if selected == "Education":
    refresh_page("edu")
    WritePath(grp.resource_path("db\\pdf\\education.pdf"))
if selected =="Health":
    refresh_page("health")
    WritePath(grp.resource_path("db\\pdf\\health.pdf"))
if selected =="WomenHealth":
    refresh_page("WHealth")
    WritePath(grp.resource_path("db\\pdf\\womenhealth.pdf"))

if voiceChat:
    VoiceChat()
    


prompt = st.chat_input("Your Query ::")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role":"user", "content" : prompt})
    full_response = get_responce(prompt, ReadPath())

    with st.chat_message("assistant"):
        
        type_message(full_response)
        st.session_state.messages.append({"role":"assistant", "content" : full_response})
