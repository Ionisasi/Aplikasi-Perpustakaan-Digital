import os
from model.dataKoleksi import KoleksiBuku
from view.UI_KoleksiBuku  import Ui_Form as Ui_BukuNonFiksi
database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")

class KoleksiNonFiksi(KoleksiBuku):
    def __init__(self):
        super().__init__(kategori="Non Fiksi", ui_class=Ui_BukuNonFiksi)
        
    def setup_search_bar(self):
        """
        Menghubungkan search bar untuk pencarian buku di Koleksi Non Fiksi.
        """
        self.ui.search.textChanged.connect(self.filter_books)