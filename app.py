from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World! Allah will help me inshallah"         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    app.run(host= '0.0.0.0')                 # run the flask app
