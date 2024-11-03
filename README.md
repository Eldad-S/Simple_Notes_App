# simple-notes-app
A simple Notes Web App using Flask and MongoDB

This is a simple Notes App I created, to learn using Flask with MongoDB.

I use Flask here as my Web Framework, and MongoDB as my Database.

I run my database inside a Docker container.

# Installation

1. First, you might want to install Docker Desktop.
2. Install an IDE of your choice (for example, VSCode).
3. Make sure you have Python installed (and Pip).
5. Clone the repo, and open it in your IDE.
6. Open a Terminal in your work folder, and run the following: 
7. python -m venv venv  # Create a Virtual Environment
8. venv\Scripts\activate (or on Linux/Mac: source venv/bin/activate) # Activate the Virtual Environment
9. pip install Flask Flask-PyMongo # Install Dependencies

# Setup

Now you are ready to setup MongoDB in a Docker container:


10. First, make sure that Docker is running properly:
11. In a new terminal, run: docker ps # Should show an empty table of containers
12. Then run: docker pull mongo
13. And: docker run -d -p 27017:27017 mongo:latest
14. Make sure the new Docker container is running (in the background) in Docker Desktop

# Run

 Now you are ready to run the Flask app:
 
 15. Go back to the first terminal, and run: python app.py

  
  Now the app is up and running, and ready to receive requests.
  
  In order to access it, go to your favorite browser, and type in the following URL:

  http://localhost:5000/notes

  This sends a GET request to your local machine, on port 5000 with the '/notes' endpoint.

  This is the main page of the app.
