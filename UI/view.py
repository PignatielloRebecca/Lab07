import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK


        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)
        # --- Sezione 2: Filtraggio ---
        musei=self.controller.handler_popola_museo()
        self.lista_musei = ft.Dropdown(label="Museo", options=[ft.dropdown.Option(m) for m in musei], expand=True,
                                       on_change = self.controller.handler_museo_changed)
        epoche=self.controller.handler_popola_epoca()
        self.lista_epoche = ft.Dropdown(label="Epoca", options=[ft.dropdown.Option(e) for e in epoche], expand=True,
                                        on_change = self.controller.handler_epoca_changed)

        self.bottone_mostra = ft.ElevatedButton(text="Mostra Artefatti", on_click= self.controller.handler_mostra_artefatti)

        # pulsante mostra artefatti

        row = ft.Row(controls=[self.lista_musei, self.lista_epoche], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
        pulsante_row=ft.Row(controls=[self.bottone_mostra],alignment=ft.MainAxisAlignment.CENTER)



        # Sezione 3: Artefatti
        self.lista_artefatti = ft.ListView(expand = True, spacing = 10, padding = 20)



        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),
            #ft.Row([self.lista_musei, self.lista_epoche], alignment=ft.MainAxisAlignment.CENTER),
            #ft.Row([self.bottone_mostra], alignment=ft.MainAxisAlignment.CENTER),

            # Sezione 2: Filtraggio
            row,
            pulsante_row,
            ft.Divider(),


            # Sezione 3: Artefatti
            self.lista_artefatti,

        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()

