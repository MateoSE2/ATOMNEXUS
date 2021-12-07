import numpy as np
import pandas as pd
import warnings

pd.set_option("display.max_rows", None, "display.max_columns", None)
warnings.filterwarnings('ignore')

from productes_db import ProductesDB, EnvasatsDB, GranelDB
from ingredients_db import IngredientsDB
from producte_ingredient_db import ProducteIngredientDB
from receptes_db import ReceptesDB
#from usuaris_db import UsuarisDB
from ingredient_recepta_db import IngredientReceptaDB
#from valoracions_db import ValoracionsDB
#from rebost_db import RebostDB

DATA_PATH = "./data/"
IMAGES_PATH = "./images/"

if __name__ == '__main__':
    print("Projecte Healthy_Life!")

    print("*" * 50)

    print("Test productes_db...")
    productes = ProductesDB(DATA_PATH + "productes_db.csv")
    productes.show()
    print("Afegint producte...")
    new_product = [999, "Producte exemple", 0, "Categoria", 1234567890987, [1.1,2.2,3.3], "envasat",  np.NaN]
    productes.add_producte(new_product)
    productes.show()
    print("Eliminant producte...")
    productes.remove_producte(999)
    productes.show()
    print("Fet!")

    print("*" * 50)

    print("Test envasats_db/granel_db...")
    envasats = EnvasatsDB(DATA_PATH + "productes_db.csv")
    granel = GranelDB(DATA_PATH + "productes_db.csv")
    print("Envasats")
    envasats.show()
    print("Granel")
    granel.show()
    print("Fet!")

    print("*" * 50)

    print("Test ingredients_db...")
    ingredients = IngredientsDB(DATA_PATH + "ingredients_db.csv")
    ingredients.show()
    print("Afegint ingredient...")
    new_ingredient = [999, "Ingredient exemple", "Descripció exemple", [1.1,2.2,3.3]]
    ingredients.add_ingredient(new_ingredient)
    ingredients.show()
    print("Eliminant ingredient...")
    ingredients.remove_ingredient(999)
    ingredients.show()
    print("Fet!")

    print("*" * 50)

    print("Test producte_ingredient_db...")
    product_ingred = ProducteIngredientDB(DATA_PATH + "producte_ingredient_db.csv")
    product_ingred.show()
    product_id = 3
    print(f"Aconseguir informació del producte {product_id} ...")
    productes.get_informacio_ingredients(product_id, product_ingred, ingredients)
    print("Fet!")

    print("*" * 50)

    print("Test ingredient_recepta_db...")
    ingred_recepta = IngredientReceptaDB(DATA_PATH + "ingredient_recepta_db.csv")
    ingred_recepta.show()
    print("Fet!")

    print("*" * 50)

    print("Test receptes_db...")
    receptes = ReceptesDB(DATA_PATH + "receptes_db.csv")
    receptes.show()
    print("Afegint recepta...")
    new_recepta = [999, "Recepta exemple", "Instruccions exemple", [1.1,2.2,3.3], 0]
    receptes.add_recepta(new_recepta)
    receptes.show()
    print("Eliminant recepta...")
    receptes.remove_recepta(999)
    receptes.show()
    #print("Aconseguint puntuació usuari...")
    id_recepta = 0
    nom_recepta = receptes.get_nom(id_recepta).item()
    print(f"Aconseguint ingredients/quantitats de la recepta '{nom_recepta}' ...")
    ing_quant = receptes.get_ingredients_and_quantitat(id_recepta, ingred_recepta, ingredients)
    print(ing_quant)
    print("Aconseguint macros...")
    macros_recepta = receptes.get_macros(id_recepta, ingred_recepta, ingredients)
    print(macros_recepta)
    print("Fet!")
