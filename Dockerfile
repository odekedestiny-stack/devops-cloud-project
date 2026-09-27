# 1. Use an official lightweight Python image as the foundation
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy our app.py script from your computer into the container
COPY app.py .

# 4. Expose port 80 so the container can accept web traffic
EXPOSE 80

# 5. The command to run our application when the container starts
CMD ["python", "app.py"]

