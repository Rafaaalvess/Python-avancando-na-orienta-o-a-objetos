from Filme import filme
from Serie import serie
from Playlist import Playlist

vingadores = filme("vingadores - guerra infinita", 2018, 160)
atlanta = serie('atlanta', 2018, 2)
tmep= filme("Todo mundo em panico", 1999, 100)
demolidor = filme('Demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

Filme_e_Series = [vingadores, atlanta,demolidor, tmep]
Playlist_Fim_de_Semana = Playlist('Fim de Semana', Filme_e_Series)

print(f'tamanho da playlist: {len(Playlist_Fim_de_Semana)}')

len(Playlist_Fim_de_Semana)

for Programa in Playlist_Fim_de_Semana:
    print(Programa)


