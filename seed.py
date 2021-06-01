from app import db
from models import Pet

db.drop_all()
db.create_all()

jackson = Pet(name="Jackson", 
              species="American Eskimo",
              photo_url="https://bit.ly/2RbvKXI")

millie = Pet(name="Millie", 
              species="Cavapoo",
              photo_url="https://bit.ly/3vG9hAV")

db.session.add_all([jackson, millie])
db.session.commit()
