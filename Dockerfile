FROM python:3.7

# Copy the contents of the current directory inside the docker image
ADD . /

# Set the home of the docker image

# Install the requirements 
RUN pip3 install -r requirements.txt 
EXPOSE 5000

# Command to run when starting the container
CMD ["python3","-u","main.py"]