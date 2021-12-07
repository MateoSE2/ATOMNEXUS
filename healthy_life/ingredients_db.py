class IngredientsDB:

  """ Init """
  def __init__(self, path):
    self._db = pd.read_csv(path,index_col=0)
    self._db_backup = self._db.copy()
    self._path = path

  """ Methods """
  def add_ingredient(self, ingredient):
    assert ingredient[0] not in self._db.id, "El id no pot estar repetit a la base de dades"
    ingredient_series = pd.Series(ingredient, index = self._db.columns)
    self._db = self._db.append(ingredient_series, ignore_index=True)
    self.save()

  def remove_ingredient(self, id):
    self._db = self._db[self._db.id != id]
    self.save()

  """ Getters """
  def get_ingredient(self, id):
    return self._db[self._db.id == id]

  def get_id(self, nom):
    return self._db[self._db.nom == nom].id

  def get_nom(self, id):
    return self._db[self._db.id == id].nom

  def get_descripcio(self, id):
    return self._db[self._db.id == id].descripcio

  def get_macros(self, id):
    return self._db[self._db.id == id].macros

  """ Setters """
  def set_descripcio(self, id, descripcio):
    self._db[self._db.id == id]["descripcio"] = descripcio

  """ Show database """
  def show(self):
    display(self._db)

  """ Reset database """
  def reset(self):
    self._db = self._db_backup
  
  """ Save database """
  def save(self):
    self._db.to_csv(self._path)
    
ingredients = IngredientsDB("/content/drive/MyDrive/Healthy Life/data/ingredients_db.csv")
def add_ingredient(ingredients):
  ingredients.add_ingredient([0,  "Macarrons",  "El macarró és un tipus de pasta italiana elaborada amb aigua, farina de blat i, a vegades, ou, que sol tenir forma de tub allargat.",                                [30, 5, 0.92]])
  ingredients.add_ingredient([1,  "Formatge",   "El formatge és un aliment sòlid que s'obté per maduració de la quallada de la llet animal o vegetal una vegada eliminat el sèrum",                                   [0, 33, 29]])
  ingredients.add_ingredient([2,  "Tomàquet",   "El tomàquet és el fruit de la tomaquera. És de color vermell, carnós i sucós, amb la superfície llisa i brillant i la polpa plena de llavors planes i groguenques.", [14.3, 1.6, 15]])
  ingredients.add_ingredient([3,  "Plàtan",     "El plàtan és una fruita comestible, de varios tipus de grans plantes del gènere Musa.",                                                                              [14.3, 1.6, 15]])
ingredients.show()
