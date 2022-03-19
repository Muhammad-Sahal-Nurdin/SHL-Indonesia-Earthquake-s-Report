import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 09 Maret 2022
    Waktu: 08:49:18 WIB
    Magnitudo: 5.2
    Kedalaman: 14 km
    Lokasi: LU= 2.57 BT=128.43
    Pusat Gempa: Pusat gempa berada di Laut 60 km TimurLaut Daruba
    Dirasakan: Dirasakan (Skala MMI): II-III Morotai
    :return:
    """
    try:
        content = requests.get('https://www.bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        waktu = result[1]
        tanggal = result[0]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 2:
                magnitudo = res.text
            elif i == 4:
                kedalaman = res.text
            elif i == 6:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 8:
                lokasi = res.text
            elif i == 10:
                dirasakan = res.text
            i = i + 2

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak dapat menampilkan data terkini.')
        return

    print('Informasi Gempa Berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: {result['lokasi']}")
    print(f"Koordinat: LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Dirasakan: {result['dirasakan']}")


if __name__ == '__main__':
    result = ekstraksi_data()
    tampilkan_data(result)
