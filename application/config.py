import os

FLASK_ENV = 'development'
DEBUG = True
TESTING = True
SECRET_KEY = os.getenv("SECRET_KEY")

db_conn_data = {"DB_USER": os.getenv("DB_USER"),
                "DB_PASSWORD": os.getenv("DB_PASSWORD"),
                "DB_HOST": os.getenv("DB_HOST"),
                "DB_PORT": os.getenv("DB_PORT")
                }
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/flask_db".format_map(db_conn_data)

SQLALCHEMY_TRACK_MODIFICATIONS = False
