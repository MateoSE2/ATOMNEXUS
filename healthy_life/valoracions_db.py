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

  def remove_valoracio(self, id_usuari, id_recepta):
    self._db = self._db[(self._db.id_usuari != id_usuari) & (self._db.id_recepta != id_recepta)]
    self.save()

  """ Getters """
  def get_receptes_usuari(self, id_usuari):
    return self._db[self._db.id_usuari == id_usuari].id_recepta

  def get_usuaris_recepta(self, id_recepta):
    return self._db[self._db.id_recepta == id_recepta].id_usuari

  def get_valoracions_recepta(self, id_recepta):
    return self._db[self._db.id_recepta == id_recepta].valoracio

  def get_valoracions_usuari(self, id_usuari):
    return self._db[self._db.id_usuari == id_usuari].valoracio

  def get_comentaris_usuari(self, id_usuari):
    return self._db[self._db.id_usuari == id_usuari].comentari

  def get_comentaris_recepta(self, id_recepta):
    return self._db[self._db.id_recepta == id_recepta].comentari

  """ Setters """
  def set_valoracio(self, id_usuari, id_recepta, valoracio):
    self._db[(self._db.id_usuari == id_usuari) & (self._db.id_recepta == id_recepta)]["valoracio"] = valoracio
    self.save()

  def set_comentari(self, id_usuari, id_recepta, comentari):
    self._db[(self._db.id_usuari == id_usuari) & (self._db.id_recepta == id_recepta)]["comentari"] = comentari
    self.save()

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
