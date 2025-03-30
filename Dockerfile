FROM python:3.11.11-bookworm


# Tells to show standard errors in logfile
ENV PYTHONUNBUFFERED=1

# Tells python not to write .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Copy all files and folders from current directory to /app directory
COPY . /app/

# Copy the requirements.txt in /app folder
COPY ./requirements.txt .

# Install all dependencies
RUN pip install -r requirements.txt

CMD ["sh", "./start.sh"]
