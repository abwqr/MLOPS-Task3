from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# # @app.route('/2')
@app.route('/add/<first>/<second>', methods=['GET'])
def func(first, second):  # put application's code here
    sum = int(first) + int(second)
    return str(sum)

@app.route('/subtract/<first>/<second>', methods=['GET'])
def subtract_route(first, second):  # put application's code here
    return int(first) - int(second)


if __name__ == '__main__':
    app.run()
