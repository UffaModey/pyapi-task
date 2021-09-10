# pyapi-task

The API is a Python REST API developed on Django web framework for an image sharing application. The API returns data in JSON format and uses SQLite for database management. The API use cases include:

1. Create a new user

http://127.0.0.1:8000/adduser/

request method: POST

    - key - username
    - Value - "name of the new user"

2. A user can uplaod an image

http://127.0.0.1:8000/upload/

request method: POST

    - key - username
        - Value - "name of user uploading image"
    - key - imageurl
        - Value - "url of the image (kittenimageurl for example)"
    - key - caption
        - Value - "image caption"

3. A user can follow another user

http://127.0.0.1:8000/follow/

request method: POST

    - key - username
        - Value - "name of following user"
    - key - followeruser
        - Value - "name of follower user"

4. A user can unfollow another user

http://127.0.0.1:8000/unfollow/

request method: POST

    - key - username
        - Value - "name of unfollowing user"
    - key - unfolloweruser
        - Value - "name of unfollowed user"
    
5. A user can like an image

http://127.0.0.1:8000/like/

request method: POST

    - key - username
        - Value - "name of user liking the image"
    - key - imageurl
        - Value - "url of image"

6. View an image

http://127.0.0.1:8000/posts/<str:imageurl>/

request method: GET

    - key - username
        - Value - "name of user liking the image"
    - key - imageurl
        - Value - "url of image"
  
7. View a user

http://127.0.0.1:8000/users/<slug:username>/

request method: GET

    - key - username
        - Value - "name of user liking the image"
    - key - imageurl
        - Value - "url of image"

### Using the API

The API was tested using Postman. To use the api:

1. Clone project GitHub repository
2. Install Django and runserver
3. Test the API urls with the approraite request methods, keys, and value pairs on Postman.
