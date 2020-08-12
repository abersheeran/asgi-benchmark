from quart import Quart

app = Quart(__name__)


@app.route("/hi/<name>")
async def hello(name):
    return f"hi {name}"
