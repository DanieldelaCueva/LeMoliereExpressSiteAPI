from django.shortcuts import render
from django.http import HttpResponseRedirect

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Articles': {
            'Create': '/articles/article-create/ [AUTHENTICATION REQUIRED]',
            'List': '/articles/all-article-list/',
            'Detail': '/articles/all-article-detail/<int:pk>/',
            'List (validated)': '/articles/validated-article-list/',
            'Detail (validated)': '/articles/validated-article-detail/<int:pk>/',
            'Update': '/articles/article-update/<int:pk>/ [AUTHENTICATION REQUIRED]',
            'Delete': '/articles/article-delete/<int:pk>/ [AUTHENTICATION REQUIRED]',
            'Validate': '/articles/article-validate/<int:pk>/ [AUTHENTICATION REQUIRED]',
            'Invalidate': '/articles/article-invalidate/<int:pk>/ [AUTHENTICATION REQUIRED]',
            'Editions List': '/articles/editions-list'
        },

        'Authorization': {
            'Login': '/authorization/login/',
            'Logout': '/authorization/logout/ [AUTHENTICATION REQUIRED]',
            'User List': '/authorization/user-list/',
            'User Detail' : '/authorization/user-detail/<str:username>/',
            'Change Password': '/authorization/change-password/<str:username>/ [AUTHENTICATION REQUIRED]'
        },

        'Docs' : {
            'Postman documentation': '/docs/'
        }
    }

    return Response(api_urls)

def docsView(request):
    return HttpResponseRedirect("https://documenter.getpostman.com/view/16803336/TzsbMTu1")