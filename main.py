from enum import Enum
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def base_get_route():
    return {'message': 'Get method'}

@app.post('/')
async def post():
    return {'message': 'Post method'}

@app.put('/')
async def put():
    return {'message': 'Put method'}

@app.get('/user')
async def list_users():
    return {'message': 'user'}

@app.get('/user/{user_id}')
async def get_user(user_id: int):
    return {'user ID': user_id}

@app.get('/me')
async def current_user():
    return {'message': "this is current user"}

class FoodEnum(str, Enum):
    vegetables = 'vegetables'
    fruits = 'fruits'
    dairy = 'dairy'    

@app.get('/food/{food_name}')
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {'food_name': food_name, 'message': 'You are healthy'}

    if food_name == FoodEnum.fruits:
        return {
            'food_name': food_name,
            'message': "You are healthy, but you like sweet things"
        }
    return {'food_name': food_name, 'message': 'I like chocolate milk'}
