from flask import Flask
app = Flask(__name__)

@app.route('/user/dongguk')
def hello_dongguk():
  return 'Hello, Dongguk University Students!'

@app.route('/user/junho')
def hello_junho():
  return 'Hello, Junho!'

if __name__ == '__main__':
  app.run()