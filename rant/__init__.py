from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ed03065f6e8248c859f6e6501792da25'


from rant import routes