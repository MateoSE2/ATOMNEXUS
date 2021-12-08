import numpy as np
import pandas as pd


class ReceptesDB:

  """ Init """
  def __init__(self, path):
    self._db = pd.read_csv(path, index_col=0)
    self._db_backup = self._db.copy()
    self._path = path

  """ Methods """
  def add_recepta(self, recepta):
    recepta_series = pd.Series(recepta, index = self._db.columns)
    self._db = self._db.append(recepta_series, ignore_index=True)
    self.save()

  def remove_recepta(self, id):
    self._db = self._db[self._db.id != id]
    self.save()

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

  def get_puntuacio_usuaris(self, id_recepta, valoracions_db):
    valoracions_db.show()
    valoracions = list(valoracions_db.get_valoracions_recepta(id_recepta))
    valoracio_mitjana = np.mean(valoracions)
    return valoracio_mitjana

  def get_ingredients_and_quantitat(self, id_recepta, ing_recep_db, ing_db):
    ingredients_list = list(ing_recep_db.get_ingredients(id_recepta))
    ing_quant_dict = {}
    for ingredient_id in ingredients_list:
        quantitat = ing_recep_db.get_quantitat(id_recepta, ingredient_id).item()
        nom = ing_db.get_nom(ingredient_id).item()
        ing_quant_dict[nom] = quantitat
    return ing_quant_dict

  def get_macros(self, id_recepta, ing_recep_db, ing_db):
    ingredients_list = ing_recep_db.get_ingredients(id_recepta)
    macros = np.array([0.0, 0.0, 0.0])
    for ingredient_id in ingredients_list:
        macros_ing = ing_db.get_macros(ingredient_id)
        macros = macros + np.array(macros_ing, dtype=float)
    return macros

  """ Setters """
  def set_instruccions(self, id, instruccions):
    self._db[self._db.id == id]["instruccions"] = instruccions
    self.save()

  def set_puntuacio_saludable(self, id, puntuacio_saludable):
    self._db[self._db.id == id]["puntuacio_saludable"] = puntuacio_saludable
    self.save()

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
