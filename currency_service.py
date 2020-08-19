from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import currency_rate_model
from timer import MultiTimer
from getter_btc import get_btc
from sqlalchemy.pool import StaticPool

class Currency_service:
    def __init__(self, db_info: str, authkey: str):
        self._authkey = authkey
        if db_info == 'sqlite:///:memory:':
            self._engine = create_engine(
                db_info,
                connect_args={"check_same_thread": False},
                poolclass=StaticPool)
        else:
            self._engine = create_engine(db_info)
        self._Base = declarative_base()
        self._Currency_rate_model = currency_rate_model.make_model(self._Base)
        self._Base.metadata.create_all(self._engine)
        self._session = sessionmaker(bind=self._engine)()
        self._timer = MultiTimer(20, self.update_now)
        self.update_now()

    def get_all(self):
        return self._session.query(self._Currency_rate_model).all()

    def get_last(self):
        return self._session.query(self._Currency_rate_model).order_by(self._Currency_rate_model.id.desc()).first()

    interval = property()

    @interval.getter
    def interval(self):
        return self._timer.interval

    @interval.setter
    def interval(self, seconds):
        self._timer.interval = seconds

    def update_now(self):
        c = get_btc(self._authkey)
        if c is not None:
            self._session.add(self._Currency_rate_model(currency = c['currency'], price = c['price']))
        return c
