# Resume
A Streamlit website that showcases my resume up to the date of the latest commit. To view the portfolio, clone the repo and follow the following steps to deploy the website locally vai Docker.

## Requirements ##
Docker

## Installation
```
docker build -t streamlit .
```

## How to Run (Docker)
```
docker run -p 8080:8080 streamlit
```

## How to Run (Local)
```
pip install -r requirements.txt
streamlit run app.py --server.port=8080 --server.address=0.0.0.0
```

Navigate to localhost:8080 (or the specified server.port) to access the website.
