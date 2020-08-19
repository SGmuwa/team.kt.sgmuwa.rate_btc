from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import currency_rate_model
from timer import MultiTimer
from getter_btc import get_btc
from sqlalchemy.pool import StaticPool
import sys
from time import sleep

class Currency_service:
    def __init__(self, db_info: str, authkey: str, interval: float):
        self._authkey = authkey
        if db_info == 'sqlite:///:memory:':
            raise Exception('«sqlite:///:memory:» dose not support.')
        for i in range(10):
            try:
                self._engine = create_engine(db_info)
            except Exception as e:
                print(e, type(e), file=sys.stderr)
                sleep(2)
                if i == 9:
                    raise
            else:
                break
        self._Base = declarative_base()
        self._Currency_rate_model = currency_rate_model.make_model(self._Base)
        for i in range(10):
            try:
                self._Base.metadata.create_all(self._engine)
            except Exception as e:
                print(e, type(e), file=sys.stderr)
                sleep(2)
                if i == 9:
                    raise
            else:
                break
        self._sessionmaker = sessionmaker(bind=self._engine)
        self._session = self._sessionmaker()
        self._timer = MultiTimer(interval, self.update_now)

    def get_all(self):
        return [c.as_dict() for c in \
            self._session \
            .query(self._Currency_rate_model) \
            .all()]

    def get_last(self):
        last = self._session \
            .query(self._Currency_rate_model) \
            .order_by(self._Currency_rate_model.id.desc()) \
            .first()
        if last is not None:
            return last.as_dict()
        return None

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
            self._session.commit()
        return c
