from pygame import mixer
from tkinter.filedialog import askopenfilename
from tkinter import *

musicas = []
TAM = len(musicas)


class Reprodutor:
    def __init__(self):
        pass

    def escolher():
        selecionar = askopenfilename(initialdir="C:/Users/%user%/desktop",
                                     filetypes=(("Arquivo de audio", "*.mp3"), ("All Files", "*.*")),
                                     title="Selecione as musicas"
                                     )
        if selecionar == '':
            pass
        else:
            musicas.append(selecionar)

    def reproduzir():
        mixer.init()

        for item in musicas:
            musica_atual = mixer.music.load(item)
            musica_atual = mixer.music.play()

    def parar():
        musica_atual = mixer.music.stop()

    def pausar():
        musica_atual = mixer.music.pause()

    def retomar():
        musica_atual = mixer.music.unpause()

    def proxima():
        global item
        item += 1

        try:
            musica_atual = mixer.music.load(musicas[item])
            musica_atual = mixer.music.play()
        except IndexError:
            item -= 1


    def anterior():
        global item
        if item - 1 == -1:
            pass
        else:
            item -= 1
        # print(item)
        musica_atual = mixer.music.load(musicas[item])
        musica_atual = mixer.music.play()


player = Reprodutor

janela = Tk()

janela.title("MUSIC PLAYER")

bt_escolher = Button(janela, width=10, text="ADICIONAR", command=player.escolher)
bt_proxima = Button(janela, width=10, text="PROXIMA", command=player.proxima)
bt_anterior = Button(janela, width=10, text="ANTERIOR", command=player.anterior)

bt_escolher.place(x=5, y=50)
bt_proxima.place(x=200, y=50)
bt_anterior.place(x=300, y=50)

bt_play = Button(janela, width=10, text="PLAY", command=player.reproduzir)
bt_pause = Button(janela, width=10, text="PAUSAR", command=player.pausar)
bt_stop = Button(janela, width=10, text="PARAR", command=player.parar)
bt_return = Button(janela, width=10, text="RETOMAR", command=player.retomar)

bt_play.place(x=5, y=0)
bt_pause.place(x=100, y=0)
bt_stop.place(x=200, y=0)
bt_return.place(x=300, y=0)

janela.geometry("410x90+450+350")
janela.mainloop()
