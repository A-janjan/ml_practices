from langchain import SerpAPIWrapper
from langchain.tools import Tool
from langchain.agents.agent_toolkits import create_retriever_tool, create_conversational_retrieval_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.chat_models import ChatGooglePalm
from langchain.embeddings import GooglePalmEmbeddings
from langchain.vectorstores import FAISS
import streamlit as st
from langchain.memory import ConversationBufferMemory


google_api_key = 'AIzaSyDmjl8e8t_kCdTwONKj0ns_07bz0AEb2L0'

st.set_page_config(page_title="GlobeBotter", page_icon=" ")

st.header(' Welcome to Globebotter, your travel assistant with Internet access. What are you planning for your next trip?')


search = SerpAPIWrapper(serpapi_api_key="1591bf80d14bd6e84796e421d712c909528dc8a0bda6309399e2342987c70f6f")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500, chunk_overlap=200)

raw_documents = PyPDFLoader(file_path="italy_travel.pdf").load()
documents = text_splitter.split_documents(raw_documents)

embeddings = GooglePalmEmbeddings(google_api_key=google_api_key)

db = FAISS.from_documents(documents, embeddings)

memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True)

llm = ChatGooglePalm(google_api_key=google_api_key)

tools = [
    Tool.from_function(
        func=search.run,
        name="Search",
        description="useful for when you need to answer questions about current events"
    ),
    create_retriever_tool(db.as_retriever(), "Italy Travel",
                          "Searches and returns doucuments reading Italy.")
]

agent = create_conversational_retrieval_agent(
    llm, tools, memory_key="chat_history", verbose=True)

user_query = st.text_input(
    "**Where are you planing your next vacation?**", placeholder="Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you?"}]

if "memory" not in st.session_state:
    st.session_state["memory"] = memory

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


def display_msg(msg, author):

    st.session_state.messages.append({"role": author, "content": msg})
    st.chat_message(author).write(msg)


if user_query:
    display_msg(user_query, 'user')
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container())
        response = agent(user_query, callbacks=[st_cb])
        st.session_state.messages.append(
            {"role": "assistant", "content": response})
        st.write(response)

if st.sidebar.button("Reset chat history"):
    st.session_state.messages = []


