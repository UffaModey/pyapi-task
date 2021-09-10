from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from imgshare.models import Posts, Users

# Create your views here.
def home(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def getposts(request, posturl):
    if request.method == 'GET':
        try:
            post = Posts.objects.get(imageurl=posturl)
            response = json.dumps([{'Post':post.imageurl, 'Caption':post.caption, 'Likes':post.likes}])
        except:
            response = json.dumps([{'Error': 'No post with that URL'}])
    return HttpResponse(response, content_type='text/json')

def getusers(request, username=' '):
    if request.method == 'GET':
        try:
            user = Users.objects.get(username=username)
            response = json.dumps([{'User': user.username,}])
        except:
            response = json.dumps([{'Error': 'No user with that name'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def adduser(request):
    payload = {}
    if request.method == 'POST':
        payload = json.loads(json.dumps(request.POST))
        newuser = payload['username']

        user = Users(username=newuser,)
        try:
            user.save()
            response = json.dumps([{'Success': 'New user created'}])
        except:
            response = json.dumps([{'Error': 'New user could not be created'}])
    return HttpResponse(response, content_type='text/json')
