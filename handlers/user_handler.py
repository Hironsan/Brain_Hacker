import tornado.web
from .base_handler import BaseHandler
from models.user import User

class UsersHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        username = self.get_argument('username', '')
        users = self.session.query(User).filter(User.name.like('%{0}%'.format(username))).all()
        self.render('user/users.html', users=users)


class UserHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        self.render('user/user.html', user=user)