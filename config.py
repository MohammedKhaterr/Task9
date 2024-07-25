class Config:
    # Database configurations
    MYSQL_HOST = 'localhost'  # Change this if your database is hosted elsewhere
    MYSQL_USER = 'your_username'  # Replace with your MariaDB username
    MYSQL_PASSWORD = 'your_password'  # Replace with your MariaDB password
    MYSQL_DB = 'contact_manager'  # The name of the database you created
    MYSQL_CURSORCLASS = 'DictCursor'  # Optional: returns rows as dictionaries
    SECRET_KEY = 'your_secret_key'  # Needed for session management
