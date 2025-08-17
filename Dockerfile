#Container base OS image
FROM python:3.9-slim

#Container working dir where application code copied
WORKDIR /app

#Copy first dependency file
COPY requirements.txt .

#Install all deps first
RUN pip install --no-cache-dir -r requirements.txt

#Copy application code to container
COPY . .

#App run on this port defined in the app code
EXPOSE 9050

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=9050

# Run app.py when the container launches
CMD ["flask", "run", "--host", "0.0.0.0"]
