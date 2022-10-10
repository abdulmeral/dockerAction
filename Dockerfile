# copy image from hub
FROM python:3.7 
# . means take all everything in dir TO appdocker
COPY . /appDocker
# working directory
WORKDIR /appDocker
RUN pip install -r requirements.txt
# run app
CMD ["python", "app.py"]