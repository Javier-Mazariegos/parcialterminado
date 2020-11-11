from flask import Flask, url_for, request,redirect
from jinja2 import Template, Environment, FileSystemLoader
import json

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Flask(__name__)

def diccionarioUso(pal: str) -> dict:
    my_data=[]
    vowel = 0
    consonants = 0
    if pal == "":
        return my_data
    palabra = pal
    reverse = palabra[::-1]
    tamaño = len(palabra)
    for i in "aeiou":
        vowel += palabra.lower().count(i)
    for i2 in "bcdfghjklmnñpqrstvwxyz":
        consonants += palabra.lower().count(i2)
    mayuscula = palabra.upper()
    minuscula = palabra.lower()
    updown = ""
    for i3 in range(len(palabra)):
        if(i3%2 == 0):
            updown += palabra[i3].upper()
        else:
            updown += palabra[i3].lower()
    naive = ""
    naive= palabra.replace("a","@")
    naive= naive.replace("e", "3")
    naive= naive.replace("i", "!")
    naive= naive.replace("o", "0")
    naive= naive.replace("u", ")")
    my_data = [palabra,reverse,tamaño,vowel,consonants,mayuscula,minuscula,updown,naive]
    return my_data



@app.route('/', methods=['GET','POST'])
def index():
    template = env.get_template('index.html')
    image_file = url_for('static',  filename ='avatar.jpg')
    my_data = []
    if request.method == 'POST':
        palabra = request.form['palabra']
        my_data = diccionarioUso(palabra)
    return template.render(my_data=my_data,image_file= image_file)


if __name__ == "__main__":
    app.run(host="localhost", port= 5000, debug=True)