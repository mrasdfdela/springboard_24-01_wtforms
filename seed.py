from app import db
from models import Pet

db.drop_all()
db.create_all()

new_pet = Pet(name="Jackson", 
              species="American Eskimo",
              photo_url="https://bit.ly/2RbvKXI")

db.session.add(new_pet)
db.session.commit()