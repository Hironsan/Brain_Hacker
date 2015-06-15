from handlers.auth_handler import LoginHandler, LogoutHandler, SignupHandler
from handlers.index_handler import IndexHandler
from handlers.search_handler import SearchHandler
from handlers.user_handler import UsersHandler, UserHandler
from handlers.group_handler import GroupsHandler, GroupHandler, GroupUserHandler
from handlers.room_handler import RoomsHandler, RoomHandler, RoomSocketHandler

from tornado.web import url

url_patterns = (
    url(r'/', IndexHandler, name='index'),
    url(r'/auth/login/', LoginHandler, name='login'),
    url(r'/auth/logout/', LogoutHandler, name='logout'),
    url(r'/auth/signup/', SignupHandler, name='signup'),
    url(r'/search/', SearchHandler, name='search'),
    url(r'/users/', UsersHandler, name='users'),
    url(r'/users/([0-9]+)/', UserHandler, name='user'),
    url(r'/groups/', GroupsHandler, name='groups'),
    url(r'/groups/([0-9]+)/', GroupHandler, name='group'),
    url(r'/groups/([0-9]+)/users/', GroupUserHandler, name='group_user'),
    url(r'/groups/([0-9]+)/rooms/', RoomsHandler, name='rooms'),
    url(r'/groups/([0-9]+)/rooms/([0-9]+)/', RoomHandler, name='room'),
    url(r'/groups/([0-9]+)/rooms/([0-9]+)/socket', RoomSocketHandler, name='room_socket'),
)