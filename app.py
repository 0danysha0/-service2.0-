from flask import Flask, render_template
from routes.predict_routes import predict_routes

app = Flask(__name__)

app.register_blueprint(predict_routes)

# Маршрут для главной страницы
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

