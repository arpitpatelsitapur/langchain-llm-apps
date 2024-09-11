from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"  # LangSmith tracking

# Fine-tuned prompt template with embedded dataset context
context = """
The Institute of Technology GGV, located in Koni, Bilaspur, is a hub of academic activity with numerous resources and services available for students. The campus is 1.4 km from the main gate, a 20-minute walk, and 8.9 km from Uslapur railway station, while Bilaspur junction is 11 km away. For administrative needs like issuing transfer certificates, students can approach the final year departmental coordinator, while queries about campus amenities such as washrooms or e-classrooms can be directed to the departmental coordinator as well. Complaints about facilities, including washroom cleaning, should be addressed to the Head of Department through a formal application. Students can book e-classrooms for events by submitting an application to the Dean of the School. Wi-Fi services, library facilities, and other amenities are managed by the respective staff, and technical support for portal access is handled by departmental coordinators.

For student activities, details about societies and clubs can be found on the GGV website or through respective senior members. Admission and placement-related questions should be directed to the Admission Coordinator or Placement Coordinator, while medical emergencies require contacting the Head of Department. Hostel allotment is merit-based for freshers, and old students can secure accommodation if they were previously hostel residents. The campus library operates from 8 am to 8 pm, and the office hours are from 10 am to 6 pm, Monday to Friday. For food services, the Swabhiman Thali offers meals between 12:30 PM and 3:00 PM, with a charge of ₹10 per meal, although online booking is not available.

Course registration for each semester can be completed through the Samarth portal, and any complaints regarding answer sheets can be addressed to the Dean through the Head of Department. The university holds an A++ NAAC ranking, offering BTech and MTech programs with fees around ₹1,25,000 and ₹71,000 respectively. Scholarships like the state scholarships, NSP, and Siemens Scholarship are available to eligible students. For bonafide certificates, students should submit an application to the department office. Wi-Fi connectivity is available on campus through MHRD, and students can register for access.
"""

# Incorporating context into the system prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", context),
        ("user", "Question: {question}")
    ]
)
# Streamlit User Interface
st.title("Student Support Q&A Chatbot (using context-based approach with LLaMA 3.1)")
input_text = st.text_input("Ask queries related to the Engineering College.")

# Using LLaMA 3.1 for the chatbot model
llm = Ollama(model="llama3.1")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Trigger the model to answer the input question based on the embedded context
if input_text:
    st.write(chain.invoke({"question": input_text}))