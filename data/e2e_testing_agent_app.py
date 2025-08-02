from flask import Flask, Response

app = Flask(__name__)

# This is the Flask route for user registration form
@app.route('/')
def index():
    with open("../data/e2e_testing_agent_register.html", "r") as html_file:
        content = html_file.read()
    return Response(content, mimetype="text/html")

if __name__ == '__main__':
    app.run(debug=True)