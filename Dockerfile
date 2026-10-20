# 1. Start with a lightweight Linux image that already has Python installed
FROM python:3.10-slim

# 2. Create a folder inside the container to hold our app
WORKDIR /app

# 3. Copy only the requirements file first 
COPY requirements.txt .

# 4. Install the Python packages inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code (app.py and the templates folder)
COPY . .

# 6. Expose the port so traffic can reach it
EXPOSE 8080

# 7. Tell the container what command to run when it starts
CMD ["python", "app.py"]
