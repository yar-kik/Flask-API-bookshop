from library import main


@main.route("/")
def hello_world():
    return "<h1>Hello world</h1>"
