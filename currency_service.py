from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import currency_rate_model

class Currency_service:
    def __init__(self):
        self._engine = create_engine('sqlite:///:memory:', echo=True)
        self._Base = declarative_base()
        self._Currency_rate_model = currency_rate_model.make_model(self._Base)
        self._Base.metadata.create_all(self._engine)
        self._session = sessionmaker(bind=self._engine)()

    def get_all(self):
        return self._session.query(self._Currency_rate_model).all()

    def get_last(self):
        return self._session.query(self._Currency_rate_model).last()

    def get_timer_interval(self):
        pass

    def set_timer_interval(self, seconds):
        pass

    def update_now(self):
        pass
