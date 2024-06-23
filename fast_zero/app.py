from fastapi import FastAPI, status

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
