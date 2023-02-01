import openai
import os
import requests
import json
import platform
import time

continue1=False
continue2=False
continue3=False
continue4=False
stop=False
main=True



print("""  ___  _           _     ___  ___  _____        ___                                            _   
 / __|| |_   __ _ | |_  / __|| _ \|_   _|      | __| _ _  __ _  _ __   ___  _ __ __  ___  _ _ | |__
| (__ |   \ / _` ||  _|| (_ ||  _/  | |        | _| | '_|/ _` || '  \ / -_) \ V  V // _ \| '_|| / /
 \___||_||_|\__/_| \__| \___||_|    |_|        |_|  |_|  \__/_||_|_|_|\___|  \_/\_/ \___/|_|  |_\_\
"""+"\n""\n""\n")

time.sleep(2)
print("""By : 
    ╔═══╗╔╗                        ╔═══╗
    ║╔═╗║║║                        ║╔═╗║
    ║╚═╝║║╚═╗╔══╗╔══╗╔═╗ ╔╗╔╗╔╗    ║║ ╚╝
    ║╔══╝║╔╗║║╔╗║║╔╗║║╔╗╗╠╣╚╬╬╝    ║║ ╔╗
    ║║   ║║║║║╚╝║║║═╣║║║║║║╔╬╬╗    ║╚═╝║
    ╚╝   ╚╝╚╝╚══╝╚══╝╚╝╚╝╚╝╚╝╚╝    ╚═══╝
                                    """+"\n""\n")

print("Please read : 'Readme.txt' first.""\n")

time.sleep(2)

my_os = platform.system()
#print("OS in my system : ",my_os)


try:
    with open(r"API.txt", 'r') as fp:
        lines = len(fp.readlines())
        print("You have "+str(lines)+" API keys available")
    if lines>1:
            text_file = open("API.txt" ,"r")
            data = text_file.read()
            text_file.close()
            nbrAPIp = data
            nbrlignec=input("Quelle API souhaitez-vous uiliser ("+nbrAPIp+") : ")
    else:
        
        if my_os=='Windows':
            try :
                text_file = open("API.txt" ,"r")
                data = text_file.read()
                text_file.close()
                APIc = data
            except :
                APIr=input("Please enter a valid API key : ")
                fichier = open("API.txt", "a")
                fichier.write(APIr)
                fichier.close()
                APIc=APIr
        if my_os=="Linux":
            if os.geteuid() != 0:
                ("You are Not Root.")
                ("Stop ChatGPTFramework...")
                StopAsyncIteration
            try:
                text_file = open("API.txt" ,"r")
                data = text_file.read()
                text_file.close()
                APIc = data
            except :
            #récupérer le chemin du répertoire courant
                path = os.getcwd()
                print("Le répertoire courant est : " + path)
                APIr=input('Rentrez une API valide : ')
                with open(path, "w") as filewrite:
                    filewrite.write(APIr)
                APIc=APIr
except:
    if my_os=='Windows':
        try :
            text_file = open("API.txt" ,"r")
            data = text_file.read()
            text_file.close()
            APIc = data
        except :
            APIr=input("Please enter a valid API key : ")
            fichier = open("API.txt", "a")
            fichier.write(APIr)
            fichier.close()
            APIc=APIr
if my_os=="Linux":
    if os.geteuid() != 0:
        ("You are Not Root.")
        ("Stop ChatGPTFramework...")
        StopAsyncIteration
    try:
        text_file = open("API.txt" ,"r")
        data = text_file.read()
        text_file.close()
        APIc = data
    except :
    #récupérer le chemin du répertoire courant
        path = os.getcwd()
        print("Le répertoire courant est : " + path)
        APIr=input('Rentrez une API valide : ')
        with open(path, "w") as filewrite:
            filewrite.write(APIr)
        APIc=APIr
    
while main:
    choix=int(input("\n""\n""1 : Utiliser ChatGPT de manière classique"+"\n"
                    "2 : Générer de Code grâce à ChatGPT"+"\n"
                    "3 : Générer un logo ou une image grâce à chatGPT"+"\n"
                    "4 : Modifier la clé API"+"\n"
                    "99 : Quitter "+"\n"
                    "GPTf : "))
    
    main=False
    if choix==1:
        continue1=True
    elif choix==2:
        continue2=True
    elif choix==3:
        continue3=True
    elif choix==4:
        continue4=True
    elif choix==99:
        stop=True
    else:
        main=True
    

if choix==1:
    while continue1:
        # Configurer une clé d'API valide
        openai.api_key = APIc

        continuer=True

        while continuer:
            # Demander à l'utilisateur de saisir une recherche
            prompt = input("Tape ta question ('exit' pour sortir) : ")
            if prompt == "exit":
                main=True
                continue1=False
                # Envoyer une requête à l'API de GPT
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=2048,
                n=1,
                stop=None,
                temperature=0.5,
            )

            # Afficher la réponse
            print("\n"+response["choices"][0]["text"]+"\n")

if choix==2:
    while continue2:
        # Configuration de l'API OpenAI
        openai.api_key = (APIc)
        # Exemple de génération de code à partir d'une description
        description = input("\n""Rentrer la description du programme à générer (exit pour sotir) : ""\n")
        if description in ("Exit",'exit'):
            main=True
            continue2=False
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=(f"{description}"),
            max_tokens=2048,
            n = 1,
            stop=None,
            temperature=0.7,
        )

        print(response["choices"][0]["text"])
  

if choix==3:
    while continue3:
        
        # Your API key
        api_key = (APIc)

         
        # The text description of the logo you want to generate
        description2 = input("\n""Entrer la description de l'image ( exit pour sotir ) : ""\n")
        if description2 in ("Exit",'exit'):
            main=True
            continue3=False
            
        # Make a request to the OpenAI API
        response = requests.post("https://api.openai.com/v1/images/generations",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            json={
                "model": "image-alpha-001",
                "prompt": description
            }
        )

        # Parse the JSON response
        response_json = json.loads(response.text)

        # Get the URL of the generated image
        image_url = response_json["data"][0]["url"]

        # Print the URL of the generated image
        print(image_url)


if choix==4:
    while continue4:
        choixr=input('Que souhaitez-vous faire ? (exit pour sortir) :'+"\n"
                        "1 : Modifier la clé "+"\n"
                        "2 : Ajouter une clé "+"\n"
                        ": ")
        if int(choixr)==1:
            APIr=input("Rentrez la nuvelle clé : ")
            fichier = open("API.txt", "w")
            fichier.write(APIr)
            fichier.close()
            APIc=APIr
        elif int(choixr)==2:
            APIr=input("Rentrez la clé à ajoutée : ")
            fichier = open("API.txt", "a")
            fichier.write(APIr)
            fichier.close()
            APIc=APIr
        elif choixr in ("Exit","exit"):
            main=True
            continue4=False

if choix==99:
    ("Stop ChatGPTFramework...")
    main=False
    continue1=False
    continue2=False
    continue3=False
    continue4=False
    stop=False

