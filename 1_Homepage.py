import streamlit as st
from datetime import date
from streamlit_timeline import timeline
# from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
# from llama_index.llms.openai import OpenAI
from constant import info, projects
from PIL import Image
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Goy's Resume' ,layout="wide", page_icon="📝")

# # -----------------  chatbot  ----------------- #
# # Set up the OpenAI key
# openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key and hit Enter', type="password")
# openai.api_key = (openai_api_key)

# # load the file
# documents = SimpleDirectoryReader(input_files=["bio.txt"]).load_data()

# name = info["Name"]
# def ask_bot(input_text):
#     # define LLM
#     llm = OpenAI(
#         model_name="gpt-3.5-turbo",
#         temperature=0,
#         openai_api_key=openai.api_key,
#     )
#     service_context = ServiceContext.from_defaults(llm=llm)

#     # load index
#     index = VectorStoreIndex.from_documents(documents, service_context=service_context)

#     # query LlamaIndex and GPT-3.5 for the AI's response
#     PROMPT_QUESTION = f"""You are an AI assistant assisting {name} in his job search by providing recruiters with relevant and concise information.
#     If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from him.
#     Don't put a breakline in the front of your answer.
#     Human: {input}
#     """

#     output = index.as_query_engine().query(PROMPT_QUESTION.format(input=input_text))
#     print(f"output: {output}")
#     return output.response


# user_input = st.text_input("Once the OpenAI API Key is provided on the sidebar, you can send your questions to know more about me using the chatbot.", key="input")

# if user_input:
#   #text = st.text_area('Enter your questions')
#   if not openai_api_key.startswith('sk-'):
#     st.warning('⚠️Please enter your OpenAI API key on the sidebar.', icon='⚠')
#   if openai_api_key.startswith('sk-'):
#     st.info(ask_bot(user_input))

# ----------------- info ----------------- #
st.header(info['Full_Name'])

with st.container():
    col1,col2=st.columns([6,5])
    with col1:
        st.markdown("""""")
        st.subheader('👋🏼 About Me')
        st.write(info['About'])
    with col2:
        st.markdown(info['Photo'],unsafe_allow_html=True)

# ----------------- education ----------------- #
with st.container():
    col1, col2, col3=st.columns([2,1,2])
    with col1:
        st.subheader('📓 Education')
        for course in info['Education']:
            st.write(f"**{course}** [{info['Education'][course]['University']}]")
            st.write(f"{info['Education'][course]['Date']}")
            st.write(f"CGPA: {info['Education'][course]['CGPA']}")
            st.markdown("""""")
    with col2:
        # -----------------  language  ----------------- #
        st.subheader('🗣️ Language')
        df=pd.DataFrame({'Language':info['Language'],'Proficiency':info['Proficiency']})

        fig, ax = plt.subplots(figsize=(3,3))
        sns.barplot(x='Language', y='Proficiency', data=df, ax=ax)
        ax.set_xlabel('Language')
        ax.set_ylabel('Proficiency')
        ax.set_title('Language Proficiency')

        # Display the chart in Streamlit
        st.pyplot(fig)

    with col3:
        for _ in range(5):
            st.markdown("""""")
        st.write(f"**English**: Professional - MUET Band 5")
        st.write(f"**Chinese**: Native")
        st.write(f"**Malay**: Conversational")

# ----------------- work experience ----------------- #
with st.container():
    st.subheader('📌 Career')

    # load data
    with open('career.json', "r") as f:
        data = json.load(f)
    data['events'][0]['end_date']={}
    data['events'][0]['end_date']['year']=str(date.today().year)
    data['events'][0]['end_date']['month']=str(date.today().month)

    # render timeline
    timeline(data, height=400)
# -----------------  project  ----------------- #
with st.container():
    st.subheader('⚒️ Projects')
    col1, col2,col3= st.columns([2,4,4])
    with col1:
        option = st.selectbox(
            "Which project are you interested in?",
            projects.keys(),
            index=None,
            placeholder="Select project",
        )
    with col2:
        if option:
            st.write(f"GitHub Link: {projects[option]['Link']}")
            st.write(f"Tools Used: ")
            for tool in projects[option]['Tools Used'].split(","):
                st.write(f"**{tool.strip()}**")
            st.write(f"Description: {projects[option]['Description']}")
    with col3:
        if option and projects[option]['Screenshot']:
            st.image(projects[option]['Screenshot'])

# -----------------  contact  ----------------- #
with st.container():
    st.subheader("📨 Contact Me")
    col1, col2= st.columns([6,5])
    with col1:
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required style="width: 500px;"><br>
            <input type="email" name="email" placeholder="Your email" required style="width: 500px;"><br>
            <textarea name="message" placeholder="Your message here" required style="width: 500px;"></textarea><br>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
    
    with col2:
        st.write(f"**Email**: {info['Email']}")
        st.write(f"**LinkedIn**: {info['LinkedIn']}")
        st.write(f"**Phone**: {info['Phone']}")
