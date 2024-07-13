import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Esercizio hotspot", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        #dd per il provider
        self._ddProvider = ft.Dropdown(label="Provider")
        self._controller.popolaDDProvider()

        # button for the "Crea Grafo" reply
        self.btn_CreaGrafo = ft.ElevatedButton(text="Crea Grafo", on_click = self._controller.handle_CreaGrafo)

        #riga 1
        row1 = ft.Row([self._ddProvider, self.btn_CreaGrafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)



        # text field for the distance
        self.txt_distanza = ft.TextField(
            label="Distanza x",
            width=200,
            hint_text="Inserisci una distanza"
        )
        self.btn_AnalisiGrafo = ft.ElevatedButton(text="Analisi Grafo", on_click=self._controller.handle_Analisi)

        #row2
        row2 = ft.Row([self.txt_distanza, self.btn_AnalisiGrafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # text field for the stringa
        self.txt_stringa = ft.TextField(
            label="Stringa s",
            width=200,
            hint_text="Inserisci una stringa"
        )
        self.btn_CalcolaPercorso = ft.ElevatedButton(text="Calcola Percorso", on_click=self._controller.handle_CalcolaPersocorso)

        # row3
        row3 = ft.Row([self.txt_stringa, self.btn_CalcolaPercorso],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # dd per il target
        self._ddTarget = ft.Dropdown(label="Target")

        #row 4
        row4 = ft.Row([self._ddTarget],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)


        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
