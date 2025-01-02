# Simple URL Shortener Project

This project is a simple URL shortener service that shortens long URLs and redirects users to the original URL when accessed. It uses a backend framework to handle URL redirection and stores mappings in a database.

## Features

- Shorten long URLs to short, unique URLs.
- Redirect users to the original URL when the short URL is accessed.
- Store URL mappings in a database.

## Technologies Used

- Python
- Flask
- SQLAlchemy
- SQLite (for database)
- HTML (for templates)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/naty1914/CodeAlpha_Simple-URL-Shortener.git
    cd CodeAlpha_Simple-URL-Shortener
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages and activate the virtual environment again:
    ```sh
    pip install -r requirements.txt
    source venv/bin/activate
    ```

4. Set up the database if not working activate the virtual environment:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

## Usage

1. Run the Flask application:
    ```sh
    flask run
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Enter a long URL in the input field and click the "Shorten" button to get a short URL.

4. Use the short URL to be redirected to the original URL.

