import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain

# Load environment variables from the .env file
load_dotenv()
key=os.getenv("OPENAI_API_KEY")

#upload PDF files
st.header('My First Chat Bot')

with st.sidebar:
    st.title('Your Document')
    file = st.file_uploader("Upload a PDF file and start asking questions", type='pdf')

# Extract the text
if file is not None:
    pdf_reader =PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
        # st.write(text)

    # Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators='\n',
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    # st.write(chunks)

    # Generating Embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=key)

    # Creating Vector Store - FAISS
    vector_store = FAISS.from_texts(chunks, embeddings)

    # Get user question
    user_question = st.text_input('type your question')

    if user_question:
        match = vector_store.similarity_search(user_question)
        # st.write(match)

        llm = ChatOpenAI(
            openai_api_key=key,
            temperature=0,
            max_tokens=1000,
            model_name='gpt-3.5-turbo'
        )

        # Output results
        chain = load_qa_chain(llm=llm, chain_type='stuff')
        response = chain.run(input_documents=match, question=user_question)
        st.write(response)

