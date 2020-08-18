
from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime

def make_model(Base):
    class CurrencyRateModel(Base):
        __tablename__ = 'currency_rate_btc_history'

        id =        Column(Integer, primary_key=True)
        stamp =     Column(DateTime, default=datetime.utcnow)
        currency =  Column(String)
        price =     Column(Float(asdecimal=True))
    
    return type(CurrencyRateModel())
