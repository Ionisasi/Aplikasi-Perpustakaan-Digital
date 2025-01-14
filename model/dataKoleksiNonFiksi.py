import os
from model.dataKoleksi import KoleksiBuku
from view.UI_KoleksiBuku  import Ui_Form as Ui_BukuNonFiksi
database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")

class KoleksiNonFiksi(KoleksiBuku):
    def __init__(self, user_id):
        super().__init__(user_id=user_id, kategori="Non Fiksi", ui_class=Ui_BukuNonFiksi)

        self.ui.headerTitle.setText("BUKU NON FIKSI")
        