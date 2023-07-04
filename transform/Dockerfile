# Use a Python base image
FROM python:3.9-slim

WORKDIR /transform

# Copy the requirements file into the container at /transform
COPY . /transform

# Set environment variables for DBT connections (adjust as needed)
ENV DBT_PROFILES_DIR=/transform/profiles
ENV DBT_PROFILE=transform

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run DBT commands when the container launches
CMD ["dbt", "run"]
