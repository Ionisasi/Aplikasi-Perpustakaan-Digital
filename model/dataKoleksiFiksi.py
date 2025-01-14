import os
from model.dataKoleksi import KoleksiBuku
from view.UI_KoleksiBuku import Ui_Form as Ui_BukuFiksi
from utils import resource_path

database_path = resource_path("database/perpusdigi.db")

class KoleksiFiksi(KoleksiBuku):
    def __init__(self, user_id):
        super().__init__(user_id=user_id, kategori="Fiksi", ui_class=Ui_BukuFiksi)

        self.ui.headerTitle.setText("BUKU FIKSI")