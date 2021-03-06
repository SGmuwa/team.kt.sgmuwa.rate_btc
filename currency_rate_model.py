from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime


def make_model(Base):
    @dataclass
    class CurrencyRateModel(Base):
        __tablename__ = 'currency_rate_btc_history'

        id =        Column(Integer, primary_key=True)
        stamp =     Column(DateTime, default=datetime.utcnow)
        currency =  Column(String(20))
        price =     Column(Float(asdecimal=True))

        def __repr__(self):
            return f"<{type(self)}(\
                id={self.id}, \
                stamp={self.stamp}, \
                currency={self.currency}, \
                price={self.price})>"

        def as_dict(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    
    return type(CurrencyRateModel())
