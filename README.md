Pour lancer le serveur :
python mysite/manage.py runserver

Pour pouvoir instancier des Images en tant que model il faut installer : python -m pip install Pillow




## BDD

Pour faire la migration :
    
    * modifier la base dans models.py
    * modifier le site d'administration dans admin.py
    * python manage.py makemigrations
    * python manage.py migrate 
    
    
    
## Exemple de commandes :

Pour prendre en compte les modifs du CSS il faut faire un CTRL+F5

### Gestion des models en shell
Microsoft Windows [version 10.0.19043.1526]
(c) Microsoft Corporation. Tous droits réservés.

(venv) D:\workspace\Django>cd mysite

(venv) D:\workspace\Django\mysite>python manage.py shell
Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from polls.models import Voie
>>> voie = Voie()
>>> voie = Voie.objects.get(name="image_name_1")
>>> voie.name
'image_name_1'
>>> voie.description
'image description 1'
>>> voie.image
<ImageFieldFile: IMG_5812.JPG>
>>> voie.image.name
'IMG_5812.JPG'
>>> voie.image.path
'D:\\workspace\\Django\\mysite\\IMG_5812.JPG'
>>> voie.image.url
'/IMG_5812.JPG'
>>>
