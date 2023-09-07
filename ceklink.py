import requests
from bs4 import BeautifulSoup

def get_google_search_links(query):
    google_search_url = f"https://www.google.com/search?q={query}"

    response = requests.get(google_search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        all_links = []
        for link in links:
            href = link.get('href')
            if href and href.startswith('/url?q='):
                url = href[7:].split('&')[0]
                all_links.append(url)

        return all_links

    else:
        print("Gagal mengambil halaman web")
        return []

while True:
    print("===================================")
    print("========== Web Scraping ===========")
    print("===================================")
    print("\n")
    print("Contoh untuk mencari situs yang mengandung kata 'slot' => site:dpr.go.id slot\n")

    query = input("Masukkan query pencarian Google: \n")

    links = get_google_search_links(query)

    if len(links) > 0:
        print("\nHasil Pencarian:")
        for i, link in enumerate(links, start=1):
            print(f"{i}. {link}")
    else:
        print("\nTidak ditemukan hasil pencarian.")

    ulangi = input("\nApakah Anda ingin melakukan pencarian lagi? (y/n): ")
    if ulangi.lower() != 'y':
        break
