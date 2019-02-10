import config
from app_initializer import initialize_data

connex_app = config.connex_app
connex_app.add_api("swagger.yml", strict_validation=True)


if __name__ == '__main__':
    initialize_data()
    connex_app.run(debug=True)
