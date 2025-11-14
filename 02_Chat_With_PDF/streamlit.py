import streamlit as st
from dotenv import load_dotenv
from app import load_pdf_data, get_text_chunks, get_vectorstore, get_conversational_chain 

load_dotenv() 

@st.cache_resource
def build_conversational_chain(text):
    texts = get_text_chunks(text)
    vector_store = get_vectorstore(texts)
    conversational_chain = get_conversational_chain(vector_store)
    return conversational_chain

def handle_user_input():
    user_question = st.text_input("Ask a question about your PDF documents:")
    return user_question

#main function to run the streamlit app
def main():
    st.set_page_config(page_title="Chat with PDF", page_icon=":books:")
    st.header("Chat with PDF :books:")
    text=""
    # upload pdf files
    with st.sidebar:
        st.subheader("Upload your PDF files here")
        pdf_docs = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
        if st.button("Process") and pdf_docs:
            with st.spinner("Processing..."):
                # load and process pdf data
                text = load_pdf_data(pdf_docs)
                conversational_chain = build_conversational_chain(text)
                st.success("PDFs processed successfully! You can now ask questions.")
        else:
            st.warning("Please upload at least one PDF file.")
    
    user_question = handle_user_input()
    if user_question:
        text = load_pdf_data(pdf_docs)
        conversational_chain = build_conversational_chain(text)
        with st.spinner("Generating answer..."):
            response = conversational_chain.run(user_question)
            st.markdown("**Answer:**")
            st.write(response)
    else:
        st.warning("Please upload and process PDF files first.")


if __name__ == "__main__":
    main()