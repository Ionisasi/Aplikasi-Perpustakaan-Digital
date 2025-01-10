# POKOKNYE JANGAN DI GANGGU DAN JANGAN DI RUN

import requests
import sqlite3
import os
from PIL import Image
from io import BytesIO
import random  # Import random untuk menghasilkan angka acak

def create_or_update_table():
    db_path = os.path.join('database', 'perpusdigi.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("PRAGMA table_info(buku)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'volume_id' not in columns:
            print("Adding 'volume_id' column to table.")
            cursor.execute(''' ALTER TABLE buku ADD COLUMN volume_id TEXT ''')
        else:
            print("Column 'volume_id' already exists.")
        
        if 'jumlah' not in columns:
            print("Adding 'jumlah' column to table.")
            cursor.execute(''' ALTER TABLE buku ADD COLUMN jumlah INTEGER ''')
        else:
            print("Column 'jumlah' already exists.")
    except sqlite3.OperationalError:
        print("Table 'buku' does not exist. Creating new table.")
        cursor.execute(''' 
            CREATE TABLE buku (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                judul TEXT,
                tahun_terbit TEXT,
                pengarang TEXT,
                penerbit TEXT,
                kategori TEXT,
                cover TEXT,
                volume_id TEXT,
                jumlah INTEGER
            )
        ''')

    conn.commit()
    conn.close()

def download_and_convert_to_png(image_url, output_folder, volume_id):
    try:
        img_data = requests.get(image_url).content
        img = Image.open(BytesIO(img_data))

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        file_name = f"{volume_id}.png"
        output_path = os.path.join(output_folder, file_name)
        img.save(output_path, 'PNG')

        return output_path
    except Exception as e:
        print(f"Error downloading or converting image: {e}")
        return None

def map_category_to_fiction_or_nonfiction(category):
    fiction_keywords = ['fiction', 'novel', 'story', 'fantasy', 'mystery', 'romance']
    nonfiction_keywords = ['science', 'history', 'biography', 'technology', 'philosophy', 'travel', 'self-help']
    category_lower = category.lower()
    if any(keyword in category_lower for keyword in fiction_keywords):
        return 'Fiksi'
    elif any(keyword in category_lower for keyword in nonfiction_keywords):
        return 'Non Fiksi'
    else:
        return 'Non Fiksi'

def get_books_and_store_to_db(query, max_results=40):
    db_path = os.path.join('database', 'perpusdigi.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    url = "https://www.googleapis.com/books/v1/volumes"
    
    start_index = 0
    total_books_fetched = 0

    while total_books_fetched < max_results:
        params = {
            'q': query,
            'startIndex': start_index,
            'langRestrict': 'id',
            'orderBy': 'relevance',
            'projection': 'full',
            'printType': 'books',
            'maxResults': min(max_results - total_books_fetched, 40)  # Ambil sisa buku yang dibutuhkan (maks 40 per permintaan)
        }

        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            books_data = response.json()
            
            # Check if 'items' key is in the response
            if 'items' not in books_data:
                print("No books found in the API response.")
                break

            cover_folder = os.path.join('Asset', 'cover-img')

            for item in books_data['items']:
                title = item['volumeInfo'].get('title', 'No Title')
                authors = ', '.join(item['volumeInfo'].get('authors', ['No Author']))
                publisher = item['volumeInfo'].get('publisher', 'No Publisher')
                published_date = item['volumeInfo'].get('publishedDate', 'No Published Date')
                categories = ', '.join(item['volumeInfo'].get('categories', ['No Category']))
                cover_url = item['volumeInfo'].get('imageLinks', {}).get('thumbnail', None)
                volume_id = item['id']

                # Periksa apakah buku memiliki cover
                if not cover_url:
                    print(f"No cover found for book '{title}'. Skipping...")
                    continue  # Lewatkan buku yang tidak memiliki cover

                # Periksa apakah buku dengan volume_id yang sama sudah ada dalam database
                cursor.execute('SELECT 1 FROM buku WHERE volume_id = ?', (volume_id,))
                if cursor.fetchone():
                    print(f"Book with volume_id {volume_id} already exists. Skipping...")
                    continue

                mapped_category = map_category_to_fiction_or_nonfiction(categories)

                cover_path = download_and_convert_to_png(cover_url, cover_folder, volume_id)

                # Generate a random number for 'jumlah' between 40 and 99
                jumlah = random.randint(40, 99)

                cursor.execute(''' 
                    INSERT INTO buku (judul, tahun_terbit, pengarang, penerbit, kategori, cover, volume_id, jumlah)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (title, published_date, authors, publisher, mapped_category, cover_path, volume_id, jumlah))

            conn.commit()
            total_books_fetched += len(books_data['items'])
            start_index += 40  # Pindah ke startIndex berikutnya

            print(f"{total_books_fetched} books fetched so far.")
        else:
            print(f"Error fetching data from Google Books API. Status code: {response.status_code}")
            print(response.text)
            break

    conn.close()

create_or_update_table()

# Example: Fetch 100 books with the query 'history or novel or mystery or science or biography or travel'
get_books_and_store_to_db('fiction or novel or story or fantasy or mystery or romance or science or history or biography', max_results=100)