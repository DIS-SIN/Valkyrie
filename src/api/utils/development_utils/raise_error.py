from flask import current_app

def raise_error(e):
    if current_app.config["ENV"] == "development":
        raise e