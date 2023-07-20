import requests
import scripts
from customtkinter import *

api_key = "db2a9e7d63aef6a482eb4c106eb8e99c"

def obter_clima(cidade):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt"
    response = requests.get(url)
    dados = response.json()
    if dados['cod']==200:
        scripts.falar("Mostrar ou falar?")
        resposta = scripts.resposta_microfone()
        if resposta == "mostrar":
            criar_janela(dados)
        elif resposta == "falar":
            scripts.falar(
                f"A temperatura na cidade de {dados['name']} é de {round(dados['main']['temp'])} graus celsius com um clima {dados['weather'][0]['description']}")
    else:
        scripts.falar("Não consegui encontrar a cidade")
def criar_janela(dados):
    janela = CTk()
    janela.resizable(False, False)
    janela.title(dados['name'])
    janela.geometry("300x300")
    janela.iconbitmap(r"C:\Users\Principal\PycharmProjects\Flora\fotos\icone.ico")



    nomeCidade = CTkLabel(janela, text=dados['name'], font=("Arial", 15), bg_color="transparent", fg_color="transparent")
    nomeCidade.grid(row=0, column=0)


    temp = CTkLabel(janela, text=f"{round(dados['main']['temp'])}ºC", font=("Arial", 50), )
    temp.grid(row=1, column=0)


    desc = dados['weather'][0]['description'].capitalize()
    desc_Clima = CTkLabel(janela, text=desc , font=("Arial", 15))
    desc_Clima.grid(row=2, column=0)

    janela.grid_columnconfigure(0, weight=1)
    janela.grid_rowconfigure(0,weight=1)
    janela.grid_rowconfigure(1,weight=1)
    janela.grid_rowconfigure(2, weight=1)


    janela.mainloop()


