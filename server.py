from flask import Flask
from db.index import get_database
from create import create_blueprint


# our Web Server Gateway Interface
app = Flask(__name__, template_folder='templates')
# the session is used to store temporary data
# to use sessions in Flask, you need to set a secret key in your application configuration
# The secret key is used to securely sign the session cookie and protect the sesssion data
app.secret_key = '123'
port = 7777


app.register_blueprint(create_blueprint, url_prefix='/create')

if __name__ == '__main__':
    # get the database
    # f-string (formatted string literal)
    print(f'Server is listening on port {port}')
    get_database()
    app.run(port=port)

   