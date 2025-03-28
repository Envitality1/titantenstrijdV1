# Titanenstrijd 2025 Website

This is a Flask web application for the Titanenstrijd 2025 event.

## Prerequisites

- Python 3.11+
- Git

## Deployment Guide

### Preparing Your Code for Deployment

1. **Push Your Code to GitHub**

   First, you need to push your code to GitHub:

   ```bash
   # If you're using GitHub CLI
   gh auth login
   gh repo create titanenstrijd-2025 --public --source=. --remote=origin
   git push -u origin main
   
   # OR using traditional Git commands
   # Create a new repository on GitHub.com first, then:
   git remote add origin https://github.com/yourusername/titanenstrijd-2025.git
   git push -u origin main
   ```

2. **Generate requirements.txt for deployment**

   Before deploying, run the included helper script to create a requirements.txt file:

   ```bash
   python export_requirements.py
   ```

### Option 1: Render.com (Recommended)

Render offers a reliable free tier for Flask applications:

1. Create an account on [Render](https://render.com)
2. Click "New Web Service"
3. Connect your GitHub repository
4. Select your repository
5. Configure with:
   - Name: titanenstrijd-2025
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn main:app`
   - Add Environment Variable: `DATABASE_URL` with your database connection string
6. Click "Create Web Service"

### Option 2: Railway.app

Railway offers a generous free tier with simple deployment:

1. Create an account on [Railway](https://railway.app)
2. Create a new project
3. Import your GitHub repository
4. Add a PostgreSQL service if needed
5. The Procfile will automatically be detected
6. Set environment variables
7. Your app will be deployed and accessible via a Railway URL

### Option 3: Fly.io

Fly.io offers a free tier with global deployment:

1. Create an account on [Fly.io](https://fly.io)
2. Install flyctl
3. Run `flyctl auth login`
4. Run `flyctl launch`
5. Configure PostgreSQL if needed
6. Deploy with `flyctl deploy`

## Local Development
1. Clone the repository: `git clone https://github.com/yourusername/titanenstrijd-2025.git`
2. Install dependencies: `pip install -e .`
3. Run the application: `python main.py`