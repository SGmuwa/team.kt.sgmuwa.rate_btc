from flask.json import JSONEncoder
import datetime
from decimal import Decimal


class CustomJSONEncoder(JSONEncoder):

  def default(self, o):
    if type(o) == datetime.timedelta:
      return str(o)
    elif type(o) == datetime.datetime:
      return o.isoformat()
    elif type(o) == Decimal:
      return str(o)
    else:
      return super().default(o)

def set_custom_json_encoder(app):
    app.json_encoder = CustomJSONEncoder
