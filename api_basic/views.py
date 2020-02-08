from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import ArticleSeralizer
from .models import Article
from rest_framework.decorators import api_view
from rest_framework import response
from rest_framework import status, request
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ARGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ArticleSeralizer
    queryset = Article.objects.all()
    lookup_field = 'id'
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, req, id):
        if id:
            return self.retrieve(request)
        else:
            return self.list(req)

    def post(self, req):
        return self.create(req)

    def put(self, req, id = None):
        return self.update(req, id)

#class based view
class ArticleAPIView(APIView):

    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSeralizer(article, many=True)
        return response.Response(serializer.data)

    def post(self, request):
        ser_lz = ArticleSeralizer(data= request.data)
        if ser_lz.is_valid():
            ser_lz.save()
            return response.Response(ser_lz.data, status=status.HTTP_201_CREATED)
        return response.Response(ser_lz.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleAPIDetails(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        article = self.get_object(id)
        seralize = ArticleSeralizer(article)
        return response.Response(seralize.data)
    def put(self,request,id):
        article = self.get_object(id)
        serialize = ArticleSeralizer(article, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return response.Response(serialize.data)
        return response.Response(serialize.errors, status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
"""
#Function based view
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        article = Article.objects.all()
        seralize = ArticleSeralizer(article, many=True)
        return response.Response(seralize.data)

    elif request.method == 'POST':
        ser_lz = ArticleSeralizer(data=request.data)
        if ser_lz.is_valid():
            ser_lz.save()
            return response.Response(ser_lz.data, status=status.HTTP_201_CREATED)
        return response.Response(ser_lz.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return response.Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        seralize = ArticleSeralizer(article)
        return response.Response(seralize.data)

    elif request.method == 'PUT':
        serialize = ArticleSeralizer(article, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return response.Response(serialize.data)
        return response.Response(serialize.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)"""

"""
@csrf_exempt
def article_list(request):

    if request.method == 'GET':
        article = Article.objects.all()
        seralize = ArticleSeralizer(article, many=True)
        return JsonResponse(seralize.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser_lz = ArticleSeralizer(data=data)

        if ser_lz.is_valid():
            ser_lz.save()
            return JsonResponse(ser_lz.data,  status=201)
        return JsonResponse(ser_lz.errors, status=400)

@csrf_exempt
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        seralize = ArticleSeralizer(article)
        return JsonResponse(seralize.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serialize = ArticleSeralizer(article,data=data)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse(serialize.data)
        return JsonResponse(serialize.errors, status=400)
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)"""
