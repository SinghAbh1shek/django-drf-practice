from django.shortcuts import render
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.paginate import LargeResultPagination, StandardResultPagination, CustomCursorPagination, paginate
from django.core.paginator import Paginator

class AuthorAPI(APIView):
    def get(self, request):
        authors = Author.objects.all()
        # paginator = StandardResultPagination()
        # paginator = LargeResultPagination()
        # paginator = CustomCursorPagination()
        # paginated_result = paginator.paginate_queryset(authors, request)

        pagenumber = request.GET.get('page', 1)
        paginator = Paginator(authors, 10)
        data = paginate(authors, paginator, pagenumber)
        serializer = AuthorSerializer(data['results'], many=True)
        data['results'] = serializer.data
        return Response({
            'status': True,
            'message': 'Data Fetched',
            # 'data': paginator.get_paginated_response(serializer.data).data,
            'data': data
        })
