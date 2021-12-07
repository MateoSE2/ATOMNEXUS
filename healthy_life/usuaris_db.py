class ReceptesDB:

  """ Init """
  def __init__(self, path):
    self._db = pd.read_csv(path, index_col=0)
    self._db_backup = self._db.copy()

  """ Methods """
  def donar_valoracio(self):
    pass

  def posar_comentari(self):
    pass

  """ Getters """
  def get_usuari(self, id):
    return self._db[self._db.id == id]

  def get_id(self, nom):
    return self._db[self._db.nom == nom].id

  def get_alies(self, id):
    return self._db[self._db.id == id].alies

  def get_nom(self, id):
    return self._db[self._db.id == id].nom

  """ Setters """
  def set_alies(self, id, alies):
    self._db[self._db.id == id]["alies"] = alies

  def set_nom(self, id, nom):
    self._db[self._db.id == id]["nom"] = nom

  """ Show database """
  def show(self):
    print(self._db)

  """ Reset database """
  def reset(self):
    self._db = self._db_backup