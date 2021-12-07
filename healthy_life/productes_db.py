class ProductesDB:

  """ Init """
  def __init__(self, path):
    self._db = pd.read_csv(path, index_col=0, converters={'macros': pd.eval})
    self._db_backup = self._db.copy()
    self._path = path

  """ Methods """
  # Add and remove products
  def add_product(self, product):
    assert product[0] not in self._db.id, "El id no pot estar repetit a la base de dades"
    product_series = pd.Series(product, index = self._db.columns)
    self._db = self._db.append(product_series, ignore_index=True)
    self.save()

  def remove_product(self, id):
    self._db = self._db[self._db.id != id]
    self.save()

  def calculate_kcalories(self, id):
    macros = self.get_macros(id)
    kcals_for_macro_type = [4, 4, 9] #1g carbs = 1g protein = 4 kcla / 1g fats = 9 kcal
    kcal = np.multiply(macros, kcals_for_macro_type).sum()
    return kcal

  """ Getters """
  def get_product(self, id):
    return self._db[self._db.id == id]

  def get_id(self, nom):
    return self._db[self._db.nom == nom].id

  def get_nom(self, id):
    return self._db[self._db.id == id].nom

  def get_qualitat(self, id):
    return self._db[self._db.id == id].qualitat

  def get_macros(self, id):
    tmp = self._db[self._db.id == id].macros
    macros = pd.eval(tmp.values)[0] #Quan guardem a csv la llista es converteix en un string, amb eval ho tornem a convertir a llista
    return macros

  def get_categoria(self, id):
    return self._db[self._db.id == id].categoria

  def get_informacio_ingredients(self, id_producte, prod_ing_db, ing_db):
    # Mirar taula producte_ingredients
    ing_id_list = list(prod_ing_db.get_ingredients(id_producte))
    print("*** LLISTA D'INGREDIENTS DEL PRODUCTE ***")
    for ingredient_id in ing_id_list:
      ing_nom =  ing_db.get_nom(ingredient_id).item()
      ing_desc = ing_db.get_descripcio(ingredient_id).item()
      print(ing_nom)
      print(ing_desc)

  """ Setters """
  def set_qualitat(self, id, qualitat):
    self._db[self._db.id == id]["qualitat"] = qualitat
    self.save()

  """ Show database """
  def show(self):
    display(self._db)

  """ Reset database """
  def reset(self):
    self._db = pd.DataFrame([], columns=self._db.columns)
    self.save()

  """ Save database """
  def save(self):
    self._db.to_csv(self._path)
    
    
class EnvasatsDB(ProductesDB):

  """ Init """
  def __init__(self,path):
    super().__init__(path)
    self._db = self._db[self._db.tipus == "envasat"]
    self._db = self._db.drop(["pes_net", "tipus"], 1)
    self._db_backup = self._db.copy()

  """ Methods """
  def get_barcode(self, id):
    return self._db[self._db.id == id].barcode

  def get_from_codebar(self, codebar):
    return self._db[self._db.codebar == codebar]

class GranelDB(ProductesDB):

  """ Init """
  def __init__(super):
    super().__init__()
    self._db = self._db[self._db.tipus == "granel"]
    self._db = self._db.drop(["codebar", "tipus"], 1)
    self._db_backup = self._db.copy()

  """ Methods """
  def obtenir_pes_net(self, id):
    return self._db[self._db.pes_net == codebar]
