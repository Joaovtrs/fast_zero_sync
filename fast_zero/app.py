import fastapi
from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

databese = []


@app.get('/', status_code=fastapi.status.HTTP_200_OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post(
    '/users/',
    status_code=fastapi.status.HTTP_201_CREATED,
    response_model=UserPublic,
)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(databese) + 1, **user.model_dump())

    databese.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': databese}


@app.get('/users/{user_id}', response_model=UserPublic)
def read_user(user_id: int):
    if user_id < 1 or user_id > len(databese):
        raise HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail='User not found',
        )

    return databese[user_id - 1]


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(databese):
        raise HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail='User not found',
        )

    user_with_id = UserDB(id=user_id, **user.model_dump())

    databese[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(databese):
        raise HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail='User not found',
        )

    del databese[user_id - 1]

    return {'message': 'User deleted'}
