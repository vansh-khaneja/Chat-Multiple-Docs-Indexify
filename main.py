import streamlit as st
from datetime import datetime
import fitz  # PyMuPDF

import dspy
from indexify import IndexifyClient,ExtractionGraph
from indexify_dspy import retriever

client = IndexifyClient()

lm = dspy.GROQ(model='mixtral-8x7b-32768', api_key ="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" )

from langchain.document_loaders import PyPDFLoader





index_name = "testdb.embeddings.embedding"


indexify_retriever_model = retriever.IndexifyRM(index_name,client)

dspy.settings.configure(lm=lm, rm=indexify_retriever_model)

def get_context(question):
    retrieve = retriever.IndexifyRM(client)
    context = retrieve(question, index_name, k=3).passages

    return context


class GenerateAnswer(dspy.Signature):
    """Answer questions with factoid answers."""

    context = dspy.InputField(desc="may contain relevant facts")
    question = dspy.InputField()
    answer = dspy.OutputField(desc="an explained answer")


class RAG(dspy.Module):
    def __init__(self, num_passages=3):
        super().__init__()
        self.retrieve = dspy.Retrieve(k=num_passages)
        self.generate_answer = dspy.ChainOfThought(GenerateAnswer)

    def forward(self, question):
        
        context = get_context(question)
        prediction = self.generate_answer(context=context, question=question)
        return dspy.Prediction(context=context, answer=prediction.answer)


uncompiled_rag = RAG()


# Function to extract file names from uploaded files
def extract_file_names(uploaded_files):
    file_names = []
    for file in uploaded_files:
        #doc = fitz.open(stream=file.read(), filetype="pdf")
        #print(file)
        file_names.append(file.name)
    return file_names




def upload_data(doc_list):

        for doc_name in doc_list:
            pdf_loader = PyPDFLoader(file_path=doc_name)
            documents = pdf_loader.load()


            for doc in documents:
                print(doc.page_content)
                content_id = client.add_documents("testdb", doc.page_content)
                client.wait_for_extraction(content_id)

# Function to generate bot response
def get_bot_response(user_input):
    # Replace this with actual logic to generate responses (e.g., API call to a language model)
    return f"Bot: {user_input}"

# Streamlit app layout
st.set_page_config(layout="wide")

# Left sidebar for PDF uploader
with st.sidebar:
    st.title("Upload PDFs")
    uploaded_files = st.file_uploader("Choose PDFs", accept_multiple_files=True, type=["pdf"])

    # Upload button
    if st.button("Upload"):
        if uploaded_files:
            file_names = extract_file_names(uploaded_files)
            upload_data(file_names)
            st.success("PDFs uploaded successfully!")
            for uploaded_file in uploaded_files:
                st.write(uploaded_file.name)
                # Here you can add code to handle the uploaded PDF files
        else:
            st.error("Please select PDFs to upload.")

# Main chat interface
st.title("Indexify Chatbot")

# User input
user_input = st.text_input("You: ", "")

# If the user submits a message
if user_input and st.button("Submit"):
    # Get bot response
    bot_response = uncompiled_rag(user_input).answer
    # Display bot response below the input box
    st.text_area("Bot response:", bot_response, height=100)
