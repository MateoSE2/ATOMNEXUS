import pandas as pd
from decode import decode_image
import cv2

class RebostDB:

  """ Init """
  def __init__(self, path):
    self._db = pd.read_csv(path, index_col=0)
    self._db_backup = self._db.copy()
    self._path = path

  """ Methods """
  def add_rebost(self, rebost):
    rebost_series = pd.Series(rebost, index = self._db.columns)
    self._db = self._db.append(rebost_series, ignore_index=True)
    self.save()
    

  def remove_rebost(self, id_usuari, id_producte):
    self._db = self._db[(self._db.id_usuari != id_usuari) & (self._db.id_producte != id_producte)]
    self.save()

  def get_productes_usuari(self, id_usuari):
     return self._db[self._db.id_usuari == id_usuari]["id_producte"]

  def get_quantitat(self, id_usuari, id_producte):
      return self._db[(self._db.id_usuari == id_usuari) & (self._db.id_producte == id_producte)]["quantitat"]

  def set_quantitat(self,id_usuari, id_producte, quantitat):
      index = self._db[(self._db.id_usuari == id_usuari) & (self._db.id_producte == id_producte)].index
      q = int(self._db.loc[index,"quantitat"])
      self._db.loc[index,"quantitat"] = int(q + quantitat)
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

  
