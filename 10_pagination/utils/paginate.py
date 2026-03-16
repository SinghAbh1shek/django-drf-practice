from rest_framework.pagination import PageNumberPagination, CursorPagination

class LargeResultPagination(PageNumberPagination):
    page_size = 100
    max_page_size = 10000

class StandardResultPagination(PageNumberPagination):
    page_size  = 10
    max_page_size = 100

class CustomCursorPagination(CursorPagination):
    page_size = 10
    ordering = 'name'
    