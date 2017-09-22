from flask import Flask
import random

app = Flask(__name_)

app.config['DEBUG'] = True

@app.route("/")
def index():
    form = """<DOCTYPE html>
    <html>
        <body>
            <form>
                <input type="text" name="input1"id="input1" />
                <label>Add Movie</label>
            </form>
        </body>
    </html>