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

  def get_productes_usuari(self, id_usuari, rebost_db, productes_db):
     productes_id = list(rebost_db.get_productes_usuari(id_usuari))
     prod_usuari_dict = {}
     for id_producte in productes_id:
         nom = productes_db.get_nom(id_producte).item()
         quantitat = rebost_db.get_quantitat(id_usuari, id_producte).item()
         prod_usuari_dict[nom] = quantitat
     return prod_usuari_dict

  """ Setters """
  def set_alies(self, id, alies):
    self._db[self._db.id == id]["alies"] = alies
    self.save()

  def set_nom(self, id, nom):
    self._db[self._db.id == id]["nom"] = nom
    self.save()

  """ Show database """
  def show(self):
    print(self._db)

  """ Reset database """
  def reset(self):
    self._db = self._db_backup

  """ Save database """
  def save(self):
    self._db.to_csv(self._path)
