from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {"message": "Welcome to Mood-Based Music Player!"}

if __name__ == '__main__':
    app.run(debug=True)