import numpy as np
import pandas as pd
import warnings
import cv2
import matplotlib.pyplot as plt
from pyzbar.pyzbar import decode

pd.set_option("display.max_rows", None, "display.max_columns", None)
warnings.filterwarnings('ignore')

from productes_db import ProductesDB, EnvasatsDB, GranelDB
from ingredients_db import IngredientsDB
from producte_ingredient_db import ProducteIngredientDB
from receptes_db import ReceptesDB
from decode import decode_image
from usuaris_db import UsuarisDB
from ingredient_recepta_db import IngredientReceptaDB
from valoracions_db import ValoracionsDB
from usuaris_db import UsuarisDB
from ingredient_recepta_db import IngredientReceptaDB
from valoracions_db import ValoracionsDB
from rebost_db import RebostDB

DATA_PATH = "./data/"
IMAGES_PATH = "./images/"

if __name__ == '__main__':
    print("Projecte Healthy_Life!")

    print("*" * 50)

    print("Test productes_db...")
    productes_db = ProductesDB(DATA_PATH + "productes_db.csv")
    productes_db.show()
    print("Afegint producte...")
    new_product = [999, "Producte exemple", 0, "Categoria", 1234567890987, [1.1,2.2,3.3], "envasat",  np.NaN]
    productes_db.add_producte(new_product)
    productes_db.show()
    print("Eliminant producte...")
    productes_db.remove_producte(999)
    productes_db.show()
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

    print("Test decode...")
    barcode_file = "./images/barcode_formatge.jpg"
    img = cv2.imread(barcode_file)
    img, _, data = decode_image(img)
	# show the image
    plt.figure()
    plt.imshow(img)
	# cv2.imwrite("barcode_detected.png", img)
    cv2.waitKey(0)
    print("Barcode data obtained:", data)
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
    productes_db.get_informacio_ingredients(product_id, product_ingred, ingredients)
    print("Fet!")

    print("*" * 50)

    print("Test ingredient_recepta_db...")
    ingred_recepta = IngredientReceptaDB(DATA_PATH + "ingredient_recepta_db.csv")
    ingred_recepta.show()
    print("Fet!")

    print("*" * 50)

    print("Test usuaris_db...")
    usuaris_db = UsuarisDB(DATA_PATH + "usuaris_db.csv")
    usuaris_db.show()
    print("Afegint usuari...")
    usuari = [999, "Joan", "Joan36"]
    usuaris_db.add_usuari(usuari)
    usuaris_db.show()
    print("Eliminant usuari...")
    usuaris_db.remove_usuari(999)
    usuaris_db.show()
    print("Fet!")

    print("*" * 50)

    print("Test valoracions...")
    valoracions_db = ValoracionsDB(DATA_PATH + "valoracions_db.csv")
    valoracions_db.show()
    print("Afegint relació usuari_recepta...")
    valoracio = [998, 999, "3", "Excel·lent!"]
    valoracions_db.add_valoracio(valoracio)
    valoracions_db.show()
    print("Eliminant relació...")
    valoracions_db.remove_valoracio(998, 999)
    valoracions_db.show()
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
    id_recepta = 0
    nom_recepta = receptes.get_nom(id_recepta).item()
    print(f"Aconseguint puntuació mitjana dels usuaris per la recepta '{nom_recepta}' ...")
    puntuacio_usuaris = receptes.get_puntuacio_usuaris(id_recepta, valoracions_db)
    print("Valoració dels usuaris:", puntuacio_usuaris)
    print(f"Aconseguint ingredients/quantitats de la recepta '{nom_recepta}' ...")
    ing_quant = receptes.get_ingredients_and_quantitat(id_recepta, ingred_recepta, ingredients)
    print(ing_quant)
    print("Aconseguint macros...")
    macros_recepta = receptes.get_macros(id_recepta, ingred_recepta, ingredients)
    print(macros_recepta)
    print("Fet!")

    print("*" * 50)

    print("Test rebost_db...")
    rebost_db = RebostDB(DATA_PATH + "rebost_db.csv")
    rebost_db.show()
    print("Afegint relació usuari_producte...")
    rebost = [998, 999, 1]
    rebost_db.add_rebost(rebost)
    rebost_db.show()
    print("Eliminant relació...")
    rebost_db.remove_rebost(998, 999)
    rebost_db.show()
    id_usuari = 0
    nom_usuari = usuaris_db.get_nom(id_usuari)
    print(f"Mostrant productes de l'usuari '{nom_usuari}' ...")
    #prod_usuari = usuaris_db.get_productes_usuari(id_usuari, rebost_db, productes_db)
    #print(prod_usuari)
    print("Fet!")

    
    print("*" * 50)
    print("Test rebost add_product_from_codebar...")

    rebost_db.add_product_from_codebar(envasats,0,barcode_file)

    print("Fet!")
    


