from rest_framework.pagination import CursorPagination
from rest_framework.pagination import PageNumberPagination

class Cursor_created(CursorPagination):
    page_size = 4
    ordering = 'created_at'
    # cursor_query_param = 'page'
    # max_page_size = 50
    # page_query_param = 'p'

class Cursor_reverse_created(CursorPagination):
    page_size = 4
    ordering = '-created_at'
    # cursor_query_param = 'page'
    # max_page_size = 50
    # page_query_param = 'p'

class Cursor_likes(CursorPagination):
    page_size = 4
    ordering = 'likes_count'
    # cursor_query_param = 'page'
    # max_page_size = 50
    # page_query_param = 'p'