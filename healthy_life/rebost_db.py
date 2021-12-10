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
    
  def add_product_from_codebar(self, envasats_db, id_usuari, path_image):
    image = cv2.imread(path_image)
    image, _, data = decode_image(image)
    producte = envasats_db.get_from_codebar(data)
    id_producte = producte.id
    quantitat = 1 # correspondrà a l'input de l'usuari a la interfície gràfica.
    self.add_rebost([id_usuari, id_producte, quantitat])

  def remove_rebost(self, id_usuari, id_producte):
    self._db = self._db[(self._db.id_usuari != id_usuari) & (self._db.id_producte != id_producte)]
    self.save()

  def get_productes_usuari(self, id_usuari):
     return self._db[self._db.id_usuari == id_usuari]["id_producte"]

  def get_quantitat(self, id_usuari, id_producte):
      return self._db[(self._db.id_usuari == id_usuari) & (self._db.id_producte == id_producte)]["quantitat"]

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
