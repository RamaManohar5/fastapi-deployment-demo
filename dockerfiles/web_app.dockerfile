# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables to avoid Python writing .pyc files to the container
ENV PYTHONDONTWRITEBYTECODE 1
# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (required for building some Python dependencies like psycopg2)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install --no-cache-dir --upgrade pip \
    && pip install pipenv

# Copy the Pipfile and Pipfile.lock first (to cache dependencies)
COPY Pipfile Pipfile.lock /app/

# Install dependencies via pipenv
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the application code into the container
COPY . /app/

