import numpy as np
import pandas as pd


class ProducteIngredientDB:

  """ Init """
  def __init__(self, path):
    self._db = pd.read_csv(path, index_col=0)
    self._db_backup = self._db.copy()
    self._path = path

  """ Method """
  def add_producte_ingredient(self, id_producte, id_ingredient):
    id_series = pd.Series([id_producte, id_ingredient], index = self._db.columns)
    self._db = self._db.append(id_series, ignore_index=True)
    self.save()

  """ Getters """
  def get_ingredients(self, id_producte):
    return self._db[self._db.id_producte == id_producte]["id_ingredient"]

  """ Show database """
  def show(self):
    print(self._db)

  """ Save database """
  def save(self):
    self._db.to_csv(self._path)
