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
