import pandas as pd

class UsuarisDB:

  """ Init """
  def __init__(self, path):
    self._db = pd.read_csv(path, index_col=0)
    self._db_backup = self._db.copy()
    self._path = path

  """ Methods """  
  def add_usuari(self, usuari):
    usuari_series = pd.Series(usuari, index = self._db.columns)
    self._db = self._db.append(usuari_series, ignore_index=True)
    self.save()

  def remove_usuari(self, id):
    self._db = self._db[self._db.id != id]
    self.save()

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
    
  """ Save database """
  def save(self):
    self._db.to_csv(self._path)