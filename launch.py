"""
Import os to gather os variables so app is able to launch.
app is the applications instance
"""
import os
from movie2archive import app

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
