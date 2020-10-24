from pony   import orm
from typing import Optional
from Database.database import User

from datetime import datetime
import bcrypt

@orm.db_session
def get_user_by_email(email: str):
    return User.get(email = email)

@orm.db_session
def register_user(new_user: User):
    User(
        email    = new_user.email,
        username = new_user.username,
        password = bcrypt.hashpw(new_user.password.encode(), bcrypt.gensalt(rounds = 6)),
        icon     = new_user.icon,
        creation_date    = new_user.creation_date,
        last_access_date = new_user.last_access_date,
        is_validated     = new_user.is_validated,
        refresh_token    = new_user.refresh_token,
        refresh_token_expires = new_user.refresh_token_expires
    )

@orm.db_session
def auth_user_password(email: str, password: str):
    try:
        user = User.get(email = email)
        return bcrypt.checkpw(password.encode(), user.password)
    except:
        return False

@orm.db_session
def activate_user(email: str, refresh_token_value: str, refresh_token_expires: datetime, last_access_date: Optional[datetime] = None):
    user = User.get(email = email)
    if last_access_date:
        user.last_access_date = last_access_date
    user.refresh_token = refresh_token_value
    user.refresh_token_expires = refresh_token_expires

@orm.db_session
def deactivate_user(email: str):
    user = User.get(email = email)
    user.refresh_token = "empty"
    user.refresh_token_expires = datetime(year = 1970, month = 1, day = 1, hour = 0, minute = 0, second = 0, microsecond = 0)

@orm.db_session
def change_username(update_data):
    if auth_user_password(update_data.email, update_data.password):
        user = User.get(email = update_data.email)
        user.username = update_data.new_username
        return user.username

@orm.db_session
def change_password(update_data):
    if auth_user_password(update_data.email, update_data.old_password):
        user = User.get(email = update_data.email)
        user.password = bcrypt.hashpw(update_data.new_password.encode(), bcrypt.gensalt(rounds = 6))
        return bcrypt.checkpw(update_data.new_password.encode(), user.password)

@orm.db_session
def change_icon(update_data, new_icon: bytes):
    if auth_user_password(update_data.email, update_data.password):
        user = User.get(email = update_data.email)
        user.icon = new_icon
        return user.icon
