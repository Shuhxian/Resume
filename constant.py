info = {
   "Full_Name": "Goy Shuh Xian",
   "About":"A data scientist currently completing my master's degree by September 2024, with experience in NLP, computer vision, generative AI, machine learning, automation, and software development projects. I am a collaborative team player with a track record of delivering results to customers in both the public and private sectors, working seamlessly with teams across different geolocations.",
   "Photo":"""<a href=\"https://www.linkedin.com/in/shuhxian/\"><img src=\"https://media.licdn.com/dms/image/C5603AQFtm4mmvLmt-Q/profile-displayphoto-shrink_800_800/0/1589787731026?e=1726099200&v=beta&t=ffyUweUnKJ3Swp3sUXcVgzC_3LIlyKJ8NfDfKb-Fdqo" width=\"200\"   alt=\"Profile\" title=\"Profile\"></a>""",
   "Email": "shuhxian@gmail.com",
   "LinkedIn": "https://www.linkedin.com/in/shuhxian/",
   "Phone": "+60164732954",
   "Github": "https://github.com/Shuhxian",
   "Language": ["English", "Chinese", "Malay"],
   "Proficiency": [5,5,4],
   "Education": {
        "Masters of Data Science":{
            "University": "Universiti Malaya",
            "Date": "October 2023 - September 2024",
            "CGPA": "4.00/4.00"
        },
        "Bachelor of Computer Science (Artificial Intelligence)":{
            "University": "Universiti Malaya",
            "Date": "September 2018 - Februrary 2022",
            "CGPA": "3.97/4.00"
        },
   }
}

projects={
    "ESG Score Prediction (Ongoing)":{
        "Link":"https://github.com/Shuhxian/ESG_score_prediction",
        "Description":"Using a dataset compiled from Bloomberg Terminal combined with Sustainalytics Risk Score extracted from Yahoo Finance API, the ESG Risk Score "+\
        "is attempted to be predicted using white-box models for full interpretability to aid investment decisions.",
        "Tools Used": "Python, Machine Learning (sklearn), SHAP",
        "Screenshot": "resources/ESG.png"
    },
    "Bank Fraud Prediction": {
        "Link":"https://github.com/Shuhxian/Bank_Fraud_Prediction_Spark",
        "Description":"Using bank account data provided by NeurIPS (https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips-2022), "+\
        "machine learning models that could detect frauds are trained using Apache Spark. The data is also analyzed using Apache Hive and visualized using Power BI.",
        "Tools Used": "Python, Apache Hive, Apache Spark, PowerBI",
        "Screenshot": "resources/BankFraud.png"
    },
    "Fraudulent Job Prediction": {
        "Link":"https://github.com/Shuhxian/fraud_job_prediction",
        "Description":"Scammers have been utilizing online job postings to target potential victims. By leveraging on machine learning models, fraudulent job postings can be "+\
        "identified to reduce the number of victims. As the data is heavily imbalanced, oversampling is required to train accurate models. The model is deployed on Streamlit and "+\
        "containerized using Docker to allow easy access.",
        "Tools Used": "Python, Machine Learning (sklearn), NLP (NLTK), Docker",
        "Screenshot": "resources/FraudJob.png"
    },
    "Car Price Prediction": {
        "Link":"https://github.com/Shuhxian/car_price_prediction",
        "Description":"By scraping data from carlist.my, prices of second hand cars along with their specifications are obtained. The data is used to train a machine learning model "+\
        "that could help to predict prices of used cars to help the public to make more informed decisions and reduce abuse by car sellers or purchasers.",
        "Tools Used": "Python, Web Scraping (BeautifulSoup), Machine Learning (sklearn), SHAP, HTML, Javascript",
        "Screenshot": "resources/CarPricePrediction.png"
    },
    "Exercise Recommendation System for Cardiac Patients": {
        "Link":"https://github.com/Shuhxian/UMFit-App",
        "Description":"Cardiac patients need to follow a strict regime to ensure they can fully recover from cardiac diseases. To ensure they stick with the exercise plan, "+\
        "exercises that are safe and enjoyable should be recommended to them. By collecting exercise preferences from cardiac patients and the elderly, combined with domain "+\
        "knowledge from doctors from PPUM, an AI-powered exercise recommendation module is developed in the form of an android app to recommend exercises which are safe and tailored.",
        "Tools Used": "Python, Flask (API), Collaborative Filtering (Surprise), Android",
        "Screenshot": "resources/ExerciseRecommendation.png"
    },
    "X-ray Covid Detection": {
        "Link":"https://github.com/Shuhxian/X-Ray-Covid-Detection",
        "Description":"Utilizing ResNet-9 architecture on Pytorch, X-ray images are classified into normal, Covid and pneumonia images to assist medical professionals in identifying respiratory "+\
        "diseases among patients.",
        "Tools Used": "Python, Image Augmentation and Classification (Pytorch)",
        "Screenshot": "resources/XRay.png"
    },
    "Bank Chatbot": {
        "Link":"https://github.com/Shuhxian/Bank_Chatbot",
        "Description":"Banks waste resources answering many redundant questions every day. The bank chatbot which is trained on scraped Q&A data from bank websites can mitigate "+\
        "this issue. The backend will preprocess the human input, find the most similar question and return the appropriate response to the user. ",
        "Tools Used": "Python, Web Scraping (BeautifulSoup), NLP (NLTK, Spacy)",
        "Screenshot": "resources/BankChatbot.png"
    },
    "Self Love App": {
        "Link":"https://github.com/Shuhxian/Self_Love_App",
        "Description":"Doing hobbies allow people to feel happy and improve spiritual health. To achieve this, questionaires are sent to university students to collect information on their behavior and hobbies. Multiclass classifier machine learning models "+\
        "are trained to predict types of hobbies that the respondents are likely to enjoy.",
        "Tools Used": "Python, Machine Learning (sklearn), Deep Learning(Tensorflow)",
        "Screenshot": ""
    },
    "Bond Price Forecasting": {
        "Link":"https://github.com/Shuhxian/bond-price-forecasting",
        "Description":"UM Hackathon 2021 - Third Place (Financial Track). Using the data provided along with other indicators scraped using Selenium such as OPR and inflation rate, " +\
        "a machine learning model is trained using Microsoft Azure to predict future price of bond prices to maximise returns of investment for financial institutions.",
        "Tools Used": "Python, Web Scraping (Selenium), Microsoft Azure",
        "Screenshot": ""
    },
    "Face Mask Detection": {
        "Link":"https://github.com/Shuhxian/Face_Mask_Detection",
        "Description":"Right after the Covid-19 pandemic, there is a need for the public to wear face masks to control the spread of the virus. To effectively ensure " + \
        "everyone adheres to the rule, this face mask detection model can be deployed in the public to bar entry of unmasked personnel.",
        "Tools Used": "Python, Image Processing (OpenCV), Deep Learning (Tensorflow)",
        "Screenshot": "resources/FaceMaskDetection.png"
    }
}