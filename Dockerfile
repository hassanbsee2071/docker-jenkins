FROM python:3

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY app.py .

# install dependencies
RUN pip install flask

# define the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./app.py"]
