from rest_framework.pagination import CursorPagination
from rest_framework.pagination import PageNumberPagination

class post_page(PageNumberPagination):
    # page_size = 9
    page_size = 6
    # test용 개수 4개
    max_page_size = 1000

class filter_modal_page(PageNumberPagination):
    page_size = 10
    max_page_size = 300

class Cursor_created(CursorPagination):
    page_size = 4
    ordering = 'likes'
    # cursor_query_param = 'page'
    max_page_size = 50
    page_query_param = 'p'

class Cursor_reverse_created(CursorPagination):
    page_size = 4
    ordering = '-created_at'
    # cursor_query_param = 'page'
    max_page_size = 50
    page_query_param = 'p'

class Cursor_likes(CursorPagination):
    page_size = 4
    ordering = ('-likes',)

    # cursor_query_param = 'page'
    max_page_size = 50
    page_query_param = 'p'

class Cursor_likes_modal(CursorPagination):
    page_size = 5
    ordering = '-created_at'


class Page_created(PageNumberPagination):
    page_size = 4
