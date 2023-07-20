import speech_recognition as sr
import requests
import re
import scripts
import pyautogui
import webbrowser as wb
from datetime import datetime
import ctypes
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import clima



def modoIzabella():

    scripts.falar("Ativando modo Izabella")
    # Minimize todas as janelas
    pyautogui.keyDown('winleft')
    pyautogui.press('d')
    pyautogui.keyUp('winleft')
   #mudança de papel de parede
    SPI_SETDESKWALLPAPER = 0x0014
    WALLPAPER_PATH = r"C:\Users\Principal\Desktop\modoIzabella.jpg"
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 1)
   #abrindo música
    wb.open("https://www.youtube.com/watch?v=AENA_nvF-L0&ab_channel=pagodepontocom")

def modoEstudo():
   scripts.falar("Ativando modo estudo")
   scripts.bloqueando_site("twitter.com")

def desativarModoEstudo():
    scripts.falar("Desativando modo estudo")
    scripts.desbloqueando_site("twitter.com")

def volumeDesejado(volume_desejado):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_desejado, None)
    scripts.falar(f"Volume alterado para {volume_desejado*100}%");

def tocar_musica(nome_musica):
    scripts.falar(f"Tocando {nome_musica} no Youtube")
    url_busca = f'https://www.youtube.com/results?search_query={nome_musica}'
    response = requests.get(url_busca)
    pattern = r'/watch\?v=([A-Za-z0-9_\-]+)'
    match = re.search(pattern, response.text)
    if match:
        video_id = match.group(1)
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        wb.open(video_url)
    else:
        print('Nenhum vídeo encontrado.')

def analise_frase(frase):
    frase= frase.lower()

    if "tocar" in frase:
        frase = frase.replace("tocar", "")
        tocar_musica(frase)

    if "que horas são" in frase:
        hora_atual = datetime.now().hour
        minuto_atual = datetime.now().minute
        scripts.falar(f"São exatamente {hora_atual} horas e {minuto_atual} minutos ")

    if "mudar volume" in frase:
        scripts.falar("para quantos por cento ?")
        novo_volume =  int(scripts.resposta_microfone())
        novo_volume = novo_volume/100
        volumeDesejado(novo_volume)

    if "ativar modo isabela" in frase:
        modoIzabella()

    if "ativar modo estudo" in frase:
        modoEstudo()

    if "desativar modo estudo" in frase:
        desativarModoEstudo()

    if "conte uma piada" in frase:
        scripts.falar(scripts.contar_piada())

    if "abrir" in frase:
        scripts.abrir(frase)

    if frase == "clima":
        scripts.falar("De qual cidade?")
        cidade = scripts.resposta_microfone()
        clima.obter_clima(cidade)

def ouvir_microfone():
   while True:
       microfone = sr.Recognizer()
       with sr.Microphone() as source:
           microfone.adjust_for_ambient_noise(source)
           audio = microfone.listen(source)
       try:
           frase = microfone.recognize_google(audio, language='pt-BR')
           print(frase)
           analise_frase(frase)
       except sr.UnknownValueError:
        print("Nada dito")



ouvir_microfone()