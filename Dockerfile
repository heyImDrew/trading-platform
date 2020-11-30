# Dockerfile

# Pull base image
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /trading_platform

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /trading_platform/
RUN pipenv install --system

# Copy project
COPY . /trading_platform/