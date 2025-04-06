from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy database setup
# PostgreSQL connection string format: postgresql://<username>:<password>@<host>:<port>/<database>
# note: there is a diffrent format required for async connection.
URL_DATABASE = 'postgresql://myuser:mypassword@localhost:5432/mydatabase'

# Create the SQLAlchemy engine
engine = create_engine(URL_DATABASE)
# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()