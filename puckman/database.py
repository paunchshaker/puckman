"""This module manages loading and creating new databases containing our
persistent data"""

from sqlalchemy import create_engine
from urllib.parse import urljoin

class Database(object):
    
    """This class stores our database connection and provides new versions"""

    def __init__(self, path=None):
        db_url = 'sqlite://'
        if path is not None:
            db_url += '/' + path

        self.engine = create_engine(db_url)

    @classmethod
    def new_db(cls, path=None):
        db = cls(path)

        from puckman.data_object import PMDataObject
        import puckman.models
        PMDataObject.metadata.create_all(db.engine)
        
        return db

    @classmethod
    def load_db(cls, path=None):
        return cls(path)

