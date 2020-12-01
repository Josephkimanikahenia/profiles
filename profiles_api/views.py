from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list APIView features"""
        an_apiview = [
        'use HTTP methods as function(get, post, patch, put, delete)',
        'is similar to a tradition django view',
        'gives you the most control over your application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
