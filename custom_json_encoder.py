from flask.json import JSONEncoder
import datetime


class CustomJSONEncoder(JSONEncoder):

  def default(self, o):
    if type(o) == datetime.timedelta:
      return str(o)
    elif type(o) == datetime.datetime:
      return o.isoformat()
    else:
      return super().default(o)

def set_custom_json_encoder(app):
    app.json_encoder = CustomJSONEncoder
