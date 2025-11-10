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
        opzione="Nessun filtro"
        musei.insert(0, opzione)
        return musei

    def handler_popola_epoca(self):
        epoche = self._model.get_epoche()
        opzione="Nessun filtro"
        epoche.insert(0, opzione)
        return epoche

    # CALLBACKS DROPDOWN
    def handler_museo_changed(self,e):
        ## aggiorna la selezione corrente del museo
        self.museo_selezionato = e.control.value # salvo il museo selezionato

    def handler_epoca_changed(self,e):
        self.epoca_selezionata = e.control.value # salvo epoca selezionata

    # AZIONE: MOSTRA ARTEFATTI

    def handler_mostra_artefatti(self,e):
        museo = self.museo_selezionato
        epoca = self.epoca_selezionata

        self._view.lista_artefatti.controls.clear()

        if museo == "Nessun filtro" and epoca == "Nessun filtro":
            artefatti = self._model.get_tutti_gli_artefatti()
            titolo = "Artefatti presenti in tutti i musei"
        else:
            #messaggio di alert per selezionare i filtri

            if not museo:
                self._view.alert.show_alert("Selezionare filtro")
                return
            if not epoca:
                self._view.alert.show_alert("Selezionare filtro")
                return

            if museo == "Nessun filtro":
                museo = None
            if epoca == "Nessun filtro":
                epoca = None

            # condizioni filtraggio

            if museo and epoca:
                artefatti = self._model.get_artefatti_filtrati(museo, epoca)
                titolo = f"Artefatti del museo '{museo}' dell'epoca '{epoca}'"
            elif museo:
                artefatti = self._model.get_artefatti_per_museo(museo)
                titolo = f"Artefatti presenti nel museo '{museo}'"
            elif epoca:
                artefatti = self._model.get_artefatti_per_epoca(epoca)
                titolo = f"Artefatti dell'epoca '{epoca}'"

        if not artefatti:
                self._view.alert.show_alert("Nessun artefatto trovato")
        else:
            #Titolo
            self._view.lista_artefatti.controls.append(ft.Text(titolo, size=18, weight="bold"))

            # Lista artefatti
            for artefatto in artefatti:
                self._view.lista_artefatti.controls.append(ft.Text(artefatto))

            self._view.update()






