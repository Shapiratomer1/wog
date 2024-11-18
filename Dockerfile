FROM python:3.9-slim

# Set working directory and copy the files to it
WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install flask requests

# expose port for Flask app
EXPOSE 8777

# Include the Scores.txt file
COPY scores.txt /scores.txt

# run the Flask app
CMD ["python", "main_score.py"]
