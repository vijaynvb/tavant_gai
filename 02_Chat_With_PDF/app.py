# implement methods for reading pdf files, converting into text chunks, embed using aws text embedding service, store in pinecone vector db

from langchain_classic.document_loaders import PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings, ChatBedrock
from dotenv import load_dotenv
from langchain_classic.vectorstores import FAISS 
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationalRetrievalChain 
from PyPDF2 import PdfReader

load_dotenv()

# function to load pdf data 
def load_pdf_data(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# function to split text into chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    texts = text_splitter.split_text(text)
    return texts
# function to embed text chunks using AWS Bedrock embeddings
def get_vectorstore(texts):
    embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0")
    vector_store = FAISS.from_texts(texts, embedding=embeddings)
    return vector_store
# function to create conversational retrieval chain
def get_conversational_chain(vector_store):
    llm = ChatBedrock(model_id="mistral.mistral-7b-instruct-v0:2")
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversational_chain = ConversationalRetrievalChain.from_llm(
        llm,
        # LC is going to facilitate retrieval from vector store and append relevant context to the LLM prompt
        vector_store.as_retriever(),
        memory=memory
    )
    return conversational_chain