FROM python:3.8-slim-buster

# set the working directory to /app
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app

# install needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# make port 80 available 
EXPOSE 80

# define environment variable
ENV NAME World

# run app.py when the container launches
CMD ["python", "app.py"]
