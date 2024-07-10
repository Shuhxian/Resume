FROM python:3.9-slim

# Expose port you want your app on
EXPOSE 8080

# Upgrade pip and install requirements
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

RUN mkdir app
WORKDIR /app
COPY 1_Homepage.py 1_Homepage.py
#COPY bio.txt bio.txt
COPY constant.py constant.py
COPY career.json career.json
COPY resources resources
COPY pages pages

# Run
ENTRYPOINT ["streamlit","run","1_Homepage.py","--server.port=8080","--server.address=0.0.0.0"]
