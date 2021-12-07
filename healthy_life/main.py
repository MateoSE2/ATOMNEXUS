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
#from usuaris_db import UsuarisDB
#from ingredients_recepta_db import IngredientsReceptaDB
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

    print("Test decode...")
    file_path = "/home/mat/Desktop/3.1/ES/PROJECTE/ATOMNEXUS/healthy_life/images/barcode_formatge.jpg"
    barcode_file = file_path
    img = cv2.imread(barcode_file)
    img, _, data = decode_image(img)
	# show the image
    plt.figure()
    plt.imshow(img)
	# cv2.imwrite("barcode_detected.png", img)
    cv2.waitKey(0)
    print("Barcode data obtained:", data)
    print("Fet!")
