import os
from src import create_app

envronment = os.environ.get("FLASK_ENV") or "production"
os.environ["FLASK_ENV"] = envronment

application = app = create_app(envronment)

if __name__ == "__main__":
    app.run()