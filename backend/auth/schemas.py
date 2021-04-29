from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('id', 'uuid', 'is_admin')
        load_only = ('password',)
        load_instance = True
