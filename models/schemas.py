from pydantic import BaseModel

class ProductPredictionRequest(BaseModel):
    title: str

class CategoryPredictionResponse(BaseModel):
    category_prediction: str

class IdPredictionResponse(BaseModel):
    id_prediction: int

