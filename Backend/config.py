import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secretive-key'
    UPLOAD_FOLDER = 'uploads/'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit upload size to 16 MB