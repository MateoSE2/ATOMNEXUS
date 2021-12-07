import numpy as np
import pandas as pd


class IngredientReceptaDB:

  """ Init """
  def __init__(self, path):
    self._db = pd.read_csv(path, index_col=0)
    self._db_backup = self._db.copy()
    self._path = path

  """ Methods """
  def add_recepta_ingredient(self, id_recepta, id_ingredient, quantitat):
    id_series = pd.Series([id_recepta, id_ingredient, quantitat], index = self._db.columns)
    self._db = self._db.append(id_series, ignore_index=True)
    self.save()

  """ Getters """
  def get_ingredients(self, id_recepta):
    return self._db[self._db.id_recepta == id_recepta]["id_ingredient"]

  def get_quantitat(self, id_recepta, id_ingredient):
    return self._db[(self._db.id_recepta == id_recepta) & (self._db.id_ingredient == id_ingredient)]["quantitat"]

  """ Show database """
  def show(self):
    print(self._db)

  """ Reset database """
  def reset(self):
    self._db = pd.DataFrame([], columns=self._db.columns)
    self.save()

  """ Save database """
  def save(self):
    self._db.to_csv(self._path)
