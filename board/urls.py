from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('board', views.board, name="board"),
    path('board_write', views.board_write, name="board_write"),
    path('board_insert', views.board_insert, name="board_insert"),
    path('board_insert_ajax', views.board_insert_ajax, name="board_insert_ajax"),
    path('board_view', views.board_view, name="board_view"),
    path('board_edit', views.board_edit, name="board_edit"),
    path('board_update', views.board_update, name="board_update"),
    path('board_delete', views.board_delete, name="board_delete"),

    path('board_ajax', views.board_ajax, name="board_ajax"),
    path('board_deleteajax', views.board_deleteajax, name="board_deleteajax"),

    path('portfolio', views.portfolio, name="portfolio"),
    path('portfolio_detail', views.portfolio_detail, name="portfolio_detail"),

]