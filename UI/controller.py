import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._providerSelected = None

    def handle_CreaGrafo(self, e):
        provider = self._view._ddProvider.value
        if provider is None:
            print("Seleziona un provider")
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Seleziona un provider."))
            self._view.update_page()
            return

        soglia = self._view.txt_distanza.value
        if soglia == "":
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Distanza non inserita."))
            self._view.update_page()
            return

        try:
            sogliaFloat = float(soglia)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Attenzione, soglia inserita non numerica."))
            self._view.update_page()
            return

        self._model.buildGraph(provider, sogliaFloat)

        nNodes, nEdges = self._model.getGraphDetails()

        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(
            ft.Text(f"Grafo correttamente creato. Il grafo ha {nNodes} nodi e {nEdges} archi."))


        self._view.update_page()


    def getNodesMostVicini(self):

        listTuples = []
        for v in self._nodes:
            listTuples.append((v, len(list(self._graph.neighbors(v)))))
        listTuples.sort(key=lambda x: x[1], reverse=True)

        # result1 = list(filter(lambda x: x[1] == listTuples[0][1] , listTuples))

        result2 = [x for x in listTuples if x[1] == listTuples[0][1]]

        # print(len(result2))
        return result2

    def getAllProviders(self):
        return self._providers

    def getAllLocations(self):
        return self._grafo.nodes

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)


    def handle_Analisi(self, e):
        pass

    def handle_CalcolaPersocorso(self,e):
        pass


    def popolaDDProvider(self):
        lista = self._model.getProviders()
        lista.sort()
        for p in lista:
            self._view._ddProvider.options.append(ft.dropdown.Option(f"{p}"))

        self._view._page.update()

        #modo2
        # providersDD = map(labda x:ft.dropdown.Option(x), providers)
         #descrizione : lambda ci indica che stiamo definendo una funzione che prende come argomento una variabile
        # x e restituisce come uscita  ft.dropdown.Option(x)
        # self._view._ddProvider.options.extend(providersDD)
        # self._view.update_page()