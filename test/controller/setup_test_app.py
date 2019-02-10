import config

app = config.app
app.testing = True
connex_app = config.connex_app
connex_app.add_api('swagger.yml', strict_validation=True)