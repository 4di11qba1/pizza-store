from mongoengine import Document, StringField, FloatField, ListField, ReferenceField

# Admin Model
class Admin(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

    def to_json(self):
        return {
            "username": self.username,
            # Avoid exposing the password
        }

# Pizza model
class Pizza(Document):
    name = StringField(required=True)
    description = StringField()
    price = FloatField(required=True)

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

class Cart(Document):
    items = ListField(ReferenceField(Pizza))  # List of pizza references
    total = FloatField(default=0.0)

class Order(Document):
    pizzas = ListField(ReferenceField(Pizza))  # List of pizza references
    total = FloatField(required=True)