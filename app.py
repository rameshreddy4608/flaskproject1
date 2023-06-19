from flask import Flask


FAI=Flask(__name__)

@FAI.route('/wish')
def wish():
    return 'This is my Flask First Project'

@FAI.route('/hello')
def hello():
    return 'hello world'


if __name__=='__main__':
    FAI.run(debug=True)