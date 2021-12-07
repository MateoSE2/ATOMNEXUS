class ReceptesDB:

  """ Init """
  def __init__(self, path):
    self._db = pd.read_csv(path, index_col=0)
    self._db_backup = self._db.copy()

  """ Methods """
  def add_recepta(self, recepta):
    recepta_series = pd.Series(recepta, index = self._db.columns)
    self._db = self._db.append(recepta_series, ignore_index=True)

  def remove_recepta(self, id):
    self._db = self._db[self._db.id != id]

  """ Getters """
  def get_recepta(self, id):
    return self._db[self._db.id == id]

  def get_id(self, nom):
    return self._db[self._db.nom == nom].id

  def get_nom(self, id):
    return self._db[self._db.id == id].nom

  def get_instruccions(self, id):
    return self._db[self._db.id == id].instruccions

  def get_temps(self, id):
     return self._db[self._db.id == id].temps

  def get_puntuacio_saludable(self, id):
     return self._db[self._db.id == id].puntuacio_saludable

  def get_puntuacio_usuaris(self, id_recepta, id_usuari):
    # mirar a taula valoracions
    pass

  def get_ingredients(self, id_recepta, id_ingredients):
    # mirar a taula ingredients_recepta
    pass

  def get_macros(self, id_recepta, id_ingredients):
    # mirar a taula ingredients_recepta
    pass

  """ Setters """
  def set_instruccions(self, id, instruccions):
    self._db[self._db.id == id]["instruccions"] = instruccions

  def set_puntuacio_saludable(self, id, puntuacio_saludable):
    self._db[self._db.id == id]["puntuacio_saludable"] = puntuacio_saludable

  """ Show database """
  def show(self):
    display(self._db)

  """ Reset database """
  def reset(self):
    self._db = self._db_backup
