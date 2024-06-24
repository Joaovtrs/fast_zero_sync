import fastapi


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == fastapi.status.HTTP_200_OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'password',
        },
    )

    assert response.status_code == fastapi.status.HTTP_201_CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == fastapi.status.HTTP_200_OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1,
            },
        ]
    }


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == fastapi.status.HTTP_200_OK
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_user_nonexistent(client):
    response = client.get('/users/2')

    assert response.status_code == fastapi.status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testusername2',
            'email': 'test@test.com',
            'password': 'password',
            'id': 1,
        },
    )

    assert response.status_code == fastapi.status.HTTP_200_OK
    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_update_user_nonexistent(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'testusername2',
            'email': 'test@test.com',
            'password': 'password',
            'id': 1,
        },
    )

    assert response.status_code == fastapi.status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == fastapi.status.HTTP_200_OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_nonexistent(client):
    response = client.delete('/users/2')

    assert response.status_code == fastapi.status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
