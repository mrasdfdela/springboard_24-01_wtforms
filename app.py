from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_life_of_pets"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adoption"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def homepage():
    """ homepage listing pets """
    pets = Pet.query.all()
    return render_template("homepage.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ form for adding adoption candidate """
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        pet = Pet(name=name,species=species,photo_url=photo_url,age=age,
        notes=notes)

        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def view_pet(pet_id):
    """ for viewing detailed pet information """
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(
      photo_url = pet.photo_url,
      notes = pet.notes,
      available = pet.available
      )

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"{pet.name} updated!")
        return redirect(f"/{pet.id}")
    else:
        return render_template("pet_details.html", pet=pet, form=form)
