from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is the Tutorial 6 EEE3095S submission for Akhtar Patel-PTLAKH001 and Takudzwa Clinton Mabika-MBKTAK003'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
