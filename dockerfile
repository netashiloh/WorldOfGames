FROM python:alpine3.13
WORKDIR /app 
COPY Utils.py ./
COPY MainScores.py ./
EXPOSE 8777
RUN pip install Flask
CMD ["python" , "MainScores.py"]