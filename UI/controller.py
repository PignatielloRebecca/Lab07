import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW 
    - Gestisce la logica del flusso dell'applicazione 
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def handler_popola_museo(self):
        musei=self._model.get_musei()
        return musei

    def handler_popola_epoca(self):
        epoche = self._model.get_epoche()
        return epoche

    # CALLBACKS DROPDOWN
    def handler_museo_changed(self,e):
        ## aggiorna la selezione corrente del museo
        self.museo_selezionato = e.control.value # salvo il museo selezionato

    def handler_epoca_changed(self,e):
        self.epoca_selezionata = e.control.value # salvo epoca selezionata

    # AZIONE: MOSTRA ARTEFATTI

    def handler_mostra_artefatti(self,e):

        if not self.museo_selezionato or not self.epoca_selezionata:
            self._view.alert.show_alert("Seleziona un museo e un'epoca.")
            return

        artefatti= self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)

        # Svuoto la lista visiva degli artefatti nella View
        self._view.lista_artefatti.controls.clear()
        # se la lista è vuota, nessun risultato trovato

        if len(artefatti)==0:
            self._view.alert.show_alert("Nessun artefatto trovato per il museo ed epoca selezionati")

        else:
            # altrimenti aggiungo un elemento per ogni artefatto trovato
            for artefatto in artefatti:
                    self._view.lista_artefatti.controls.append(ft.Text(artefatto))
            self._view.update()





