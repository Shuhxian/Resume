import streamlit as st
import os
import google.generativeai as genai

st.set_page_config(page_title="Goy's Resume" ,layout="wide", page_icon="📝")

st.header("Chatbot")

key = st.sidebar.text_input('Enter your Gemini API Key and hit Enter', type="password")
genai.configure(api_key=key)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

text=st.text_input("Question")
if text:
  if not key: 
    st.error("Please enter your Gemini API Key")
  else:
    response = model.generate_content([
      "input: What is his skills?",
      "output: Goy has experience in NLP, computer vision, generative AI, machine learning, automation, and software development projects. He is proficient in Python and its machine learning frameworks, and has experience using big data technologies such as Apache Spark and Hive, and cloud technologies such as AWS and Google Cloud Platform.",
      "input: When would Goy be available for work?",
      "output: Goy currently has a 3 month notice period, but you may reach out to him to discuss on opportunities and he can make appropriate arrangements.",
      "input: What is his education level?",
      "output: Goy graduated with a degree in computer science (AI) in Universiti Malaya and will be completing his master's in data science in September 2024.",
      "input: Is Goy willing to relocate?",
      "output: Goy is willing to relocate if the company could sponsor his visa and employment pass.",
      "input: What roles are you interested in?",
      "output: Goy is open to roles related to data science, AI and/or related to cloud development.",
      "input: Where has Goy worked at?",
      "output: Goy is currently employed as a Data Scientist in Inventech Digital and has worked in Core Consulting as an Automation Engineer, Intel Microelectronics as a Customer Software Enabling and Optimization Engineer and Moneylion as a Data Scientist intern.",
      "input: What are Goy's language proficiency?",
      "output: Goy is native in Chinese but can speak English and Malay fluently. Fun fact, also learns Japanese and French using Duolingo!",
      "input: What is Goy's strengths?",
      "output: Goy is a firm believer of 1+1>2. He believes in teamwork and contributes ideas and work together as a team to drive success in the team and deliver value to customers.",
      "input: What is Goy/s proudest achievements?",
      "output: Goy represented Intel Microelectronics in Semicon 2023, one of the largest industry events in Malaysia. The exercise recommendation system that was developed as his final year project was actually planned to be tested in PPUM (Universiti Malaya) hospital.",
      "input: Are you available for other opportunities?",
      "output: Goy is open for other opportunities, please leave a message for him via email or LinkedIn.",
      "input: What is your contact method?",
      "output: You may reach out to Goy at shuhxian@gmail.com, +60164732954, or on LinkedIn.",
      "input: Who are your referrals?",
      "output: Please approach Goy if you require referrals.",
      "input: How did you create this Chatbot?",
      "output: The chatbot is powered by Gemini developed by Google and is fine-tuned using data from the resume.",
      "input: Where is Goy based at?",
      "output: Goy is currently based at Petaling Jaya, Selangor, Malaysia currently, but is willing to relocate.",
      "input: What is Goy's interest?",
      "output: Goy likes to learn new things, from the newest technology to different languages and cultures. To live is to learn.",
      "input: What is Goy's favorite quote?",
      "output: \"It is not about who you are, but what you do that defines you.\" -Bruce Wayne",
      "input: Which countries have you worked with before?",
      "output: Goy had worked with colleagues from the US, India, Taiwan and others throughout his career. With his cultural knowledge, Goy can get along well with people from diverse backgrounds.",
      "input: What is your MBTI?",
      "output: Goy is an INTP individual.",
      "input: What is your expected salary?",
      "output: It depends on the role and the country. All in all, as long as the career is exciting and the offer is reasonable, it can be considered.",
      "input: Why do you want to be a data scientist?",
      "output: Goy wants to use data to discover insights and to drive better decision making and make an impact in businesses and to the society.",
      "input: "+text,
      "output: ",
    ])
    st.write(response.text)
