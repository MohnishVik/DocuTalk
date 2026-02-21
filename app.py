import os
import PyPDF2
import chainlit as cl
from dotenv import load_dotenv

# LangChain + Groq
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import ChatMessageHistory


# -------------------------
# Load Environment Variables
# -------------------------
load_dotenv()
groq_api_key = os.environ["GROQ_API_KEY"]


# -------------------------
# Initialize Groq LLM
# -------------------------
llm_groq = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant",
    temperature=0.2
)


# -------------------------
# On Chat Start
# -------------------------
@cl.on_chat_start
async def on_chat_start():

    # Display Banner Image
    elements = [
        cl.Image(
            name="DocuTalk Banner",
            path="screen-0.jpg",  # Make sure file is in same folder
            display="inline"
        )
    ]

    await cl.Message(
        content="📄 **Welcome to DocuTalk!**\n\nUpload your PDFs to begin.",
        elements=elements
    ).send()

    # Wait for PDF Upload
    files = None
    while files is None:
        files = await cl.AskFileMessage(
            content="Please upload one or more PDF files",
            accept=["application/pdf"],
            max_files=10,
            max_size_mb=100,
        ).send()

    texts = []
    metadatas = []

    # Process PDFs
    for file in files:
        pdf = PyPDF2.PdfReader(file.path)
        pdf_text = ""

        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pdf_text += text

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200,
            chunk_overlap=100
        )

        chunks = splitter.split_text(pdf_text)

        texts.extend(chunks)
        metadatas.extend(
            [{"source": f"{file.name} - chunk {i}"} for i in range(len(chunks))]
        )

    # -------------------------
    # Embeddings (Production Ready)
    # -------------------------
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create Vector Store
    docsearch = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas
    )

    # Memory for conversation
    memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    chat_memory=ChatMessageHistory(),
    output_key="answer"   
)

    # Conversational Retrieval Chain
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm_groq,
        retriever=docsearch.as_retriever(),
        memory=memory,
        return_source_documents=True
    )

    cl.user_session.set("chain", chain)

    await cl.Message(
        content="✅ PDFs processed successfully! You can now ask questions."
    ).send()


# -------------------------
# On User Message
# -------------------------
@cl.on_message
async def main(message: cl.Message):

    chain = cl.user_session.get("chain")

    if not chain:
        await cl.Message(
            content="⚠️ Please upload PDF files first."
        ).send()
        return

    # Invoke Chain
    response = await chain.ainvoke({"question": message.content})

    answer = response["answer"]
    source_docs = response.get("source_documents", [])

    text_elements = []

    if source_docs:
        for idx, doc in enumerate(source_docs):
            text_elements.append(
                cl.Text(
                    content=doc.page_content,
                    name=f"source_{idx}"
                )
            )

        answer += "\n\n📚 **Sources attached below.**"

    await cl.Message(
        content=answer,
        elements=text_elements
    ).send()