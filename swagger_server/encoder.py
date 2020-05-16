from connexion.apps.flask_app import FlaskJSONEncoder

from swagger_server.models.base_model_ import Model


class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, Model):
            return self.encode_model(o)
        return FlaskJSONEncoder.default(self, o)

    def encode_model(self, o: Model):
        dikt = {}
        for attr in o.swagger_types.keys():
            value = getattr(o, attr)
            if value is None and not self.include_nulls:
                continue
            attr = o.attribute_map[attr]
            dikt[attr] = value
        return dikt
