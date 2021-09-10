from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from imgshare.models import Posts, Users

# Create your views here.
def home(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def getposts(request, imageurl):
    if request.method == 'GET':
        try:
            post = Posts.objects.get(imageurl=imageurl)
            response = json.dumps([{'Post':post.imageurl, 'Caption':post.caption, 'Likes':post.likes}])
        except:
            response = json.dumps([{'Error': 'No post with that URL'}])
    return HttpResponse(response, content_type='text/json')

def getusers(request, username):
    if request.method == 'GET':
        try:
            user = Users.objects.get(username=username)
            response = json.dumps([{'User': user.username, 'Following': user.following, 'Followers': user.followers,}])
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

@csrf_exempt
def follow(request):
    payload = {}
    if request.method == 'POST':
        payload = json.loads(json.dumps(request.POST))
        username = payload['username']
        followuser = payload['followuser']

        try:
            user = Users.objects.get(username = username)
            user.following = followuser
            user.save()

            follower = Users.objects.get(username = followuser)
            follower.followers = username
            follower.save()
            response = json.dumps([{'Success': 'Following updated'}])
        except:
            response = json.dumps([{'Error': 'Users not found'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def unfollow(request):
    payload = {}
    if request.method == 'POST':
        payload = json.loads(json.dumps(request.POST))
        username = payload['username']
        unfollowuser = payload['unfollowuser']
        user = Users.objects.get(username = username)
        
        try:
            if user.following == unfollowuser:
                user.following = ""

                follower = Users.objects.get(username = unfollowuser)
                if follower.followers == username:
                    follower.followers = ""
                    response = json.dumps([{'Success': 'user unfollowed'}])
        except:
            response = json.dumps([{'Error': 'Users not found'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def uploadimg(request):
    payload = {}
    if request.method == 'POST':
        payload = json.loads(json.dumps(request.POST))
        user = payload['username']
        imageurl = payload['imageurl']
        caption = payload['caption']

        try:
            data = Users.objects.all()
            for i in data:
                if  i.username == user:
                    upload = Posts(imageurl=imageurl, caption = caption, likes = 0)
                    upload.save()
                    response = json.dumps([{'Success': 'Image uploaded'}])
                else:
                    response = json.dumps([{'Error': 'No user found'}])
        except:
            response = json.dumps([{'Error': 'invalid values'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def like(request):
    payload = {}
    if request.method == 'POST':
        payload = json.loads(json.dumps(request.POST))
        user = payload['username']
        imageurl = payload['imageurl']

        try:
            data = Users.objects.get(username = user)
            posts = Posts.objects.get(imageurl = imageurl)
            posts.likes = posts.likes + 1
            posts.save()
            response = json.dumps([{'Success': 'image liked'}])
        except:
            response = json.dumps([{'Error': 'invalid values'}])
    return HttpResponse(response, content_type='text/json')
