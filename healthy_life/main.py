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
<<<<<<< HEAD
from usuaris_db import UsuarisDB
#from ingredients_recepta_db import IngredientsReceptaDB
from valoracions_db import ValoracionsDB
=======
#from usuaris_db import UsuarisDB
from ingredient_recepta_db import IngredientReceptaDB
#from valoracions_db import ValoracionsDB
>>>>>>> af65f4db6474fb7c9c259473423726322e130cfc
#from rebost_db import RebostDB

DATA_PATH = "./data/"
IMAGES_PATH = "./images/"
GERARD_LL_ROOT = ""
GERARD_G_ROOT = ""
MATEO_ROOT = "/home/mat/Desktop/3.1/ES/PROJECTE/ATOMNEXUS/"

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
    productes.get_informacio_ingredients(product_id, product_ingred, ingredients)
    print("Fet!")

    print("*" * 50)

    print("Test ingredient_recepta_db...")
    ingred_recepta = IngredientReceptaDB(DATA_PATH + "ingredient_recepta_db.csv")
    ingred_recepta.show()
    print("Fet!")
    
    print("Test usuaris...")
    file_path = "C:/Users/gerar/ATOMNEXUS/healthy_life/data/usuaris_db.csv"
    usuaris_db = UsuarisDB(file_path)
    print("Creem l'usuari de prova...")
    usuari = [999, "Joan", "Joan36"]
    usuaris_db.add_usuari(usuari)
    print("Mostrem l'usuari de prova...")
    usuaris_db.show()
    print("Eliminem l'usuari de prova i comprovem que el dataset està buit...")
    usuaris_db.remove_usuari(usuari[0])
    usuaris_db.show()
    print("Fet!")
    
    print("Test valoracions...")
    file_path = "C:/Users/gerar/ATOMNEXUS/healthy_life/data/valoracions_db.csv"
    valoracions_db = ValoracionsDB(file_path)
    print("Creem l'usuari de prova...")
    valoracio = [998, 999, "3", "Excel·lent!"]
    valoracions_db.add_valoracio(valoracio)
    print("Mostrem l'usuari de prova...")
    valoracions_db.show()
    print("Eliminem l'usuari de prova i comprovem que el dataset està buit...")
    valoracions_db.reset()
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

    print("*" * 50)