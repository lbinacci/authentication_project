from flask_login import UserMixin


class User(UserMixin):
   def __init__(self, id, username, password, email):
      self.id = id
      self.username = username
      self.password = password
      self.email = email

   def is_authenticated(self):
      return True
   def is_anonymous(self):
      return False

