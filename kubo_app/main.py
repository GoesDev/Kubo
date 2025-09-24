from flask import Flask, render_template, request
from routes import app

if __name__ == '__main__':
    app.run(debug=True)
