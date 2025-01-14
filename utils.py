import os
import sys

def resource_path(relative_path):
    """Mengakses resource, baik di lingkungan dev maupun executable"""
    if getattr(sys, 'frozen', False):  # Jika sudah dalam bentuk executable
        base_path = sys._MEIPASS  # Direktori sementara untuk file resource
    else:
        base_path = os.path.abspath(".")  # Lokasi file saat pengembangan

    return os.path.join(base_path, relative_path)

