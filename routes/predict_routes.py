from flask import Blueprint, request, jsonify
from models.schemas import ProductPredictionRequest, CategoryPredictionResponse, IdPredictionResponse
import joblib

predict_routes = Blueprint('predict_routes', __name__)

# Загрузка обученных моделей и векторизатора
model_category = joblib.load("model_label.joblib")
model_id = joblib.load("model_id.joblib")
vectorizer = joblib.load("vectorizer.joblib")

@predict_routes.route('/predict_category', methods=['POST'])
def predict_category():
    data = request.json
    request_data = ProductPredictionRequest(**data)
    title = request_data.title

    # Векторизация
    title_vectorized = vectorizer.transform([title])
    # Предсказание категории
    category_prediction = model_category.predict(title_vectorized)

    response_data = CategoryPredictionResponse(category_prediction=category_prediction[0])
    return jsonify(response_data.dict())

@predict_routes.route('/predict_id', methods=['POST'])
def predict_id():
    data = request.json
    request_data = ProductPredictionRequest(**data)
    title = request_data.title

    # Векторизация
    title_vectorized = vectorizer.transform([title])
    # Предсказание ID категории
    id_prediction = model_id.predict(title_vectorized)

    response_data = IdPredictionResponse(id_prediction=id_prediction[0])
    return jsonify(response_data.dict())

