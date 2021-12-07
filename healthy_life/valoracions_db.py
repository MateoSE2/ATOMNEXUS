import pandas as pd

class ValoracionsDB:

  """ Init """
  def __init__(self, path):
    self._db = pd.read_csv(path, index_col=0)
    self._db_backup = self._db.copy()
    self._path = path

  """ Methods """
  def add_valoracio(self, valoracio):
    valoracio_series = pd.Series(valoracio, index = self._db.columns)
    self._db = self._db.append(valoracio_series, ignore_index=True)
    self.save()

  def remove_valoracio(self, id):
    self._db = self._db[self._db.id != id]
    self.save()
    
  """ Getters """
  def get_obj_valoracio(self, id):
    return self._db[self._db.id == id]

  def get_id_usuari(self, nom):
    pass

  def get_id_recepta(self, nom):
    pass

  def get_valoracio(self, id):
    return self._db[self._db.id == id].valoracio

  def get_comentari(self, id):
    return self._db[self._db.id == id].comentari

  """ Setters """
  def set_valoracio(self, id, valoracio):
    self._db[self._db.id == id]["valoracio"] = valoracio

  def set_comentari(self, id, comentari):
    self._db[self._db.id == id]["comentari"] = comentari

  """ Show database """
  def show(self):
    print(self._db)

  """ Reset database """
  def reset(self):
    self._db = self._db_backup
    self.save()
    
  """ Save database """
  def save(self):
    self._db.to_csv(self._path)