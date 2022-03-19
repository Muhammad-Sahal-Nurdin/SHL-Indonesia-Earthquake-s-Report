# SHL-Indonesia-Earthquake's-Report
This is a live earthquake report from Indonesian Agency for Meteorology, Climatology, and Geophysics' s data

## How this Program Work?
this package will extract data from [BMKG](https://www.bmkg.go.id)

this program will retrieve data from bmkg using the beautiful4 library and request.

# How To Use
import gempa_terkini

if  __name__ == '__main__':
    print('Aplikasi Utama')
    result = gempa_terkini.ekstraksi_data()
    gempa_terkini.tampilkan_data(result)

# Author
Muhammad Sahal Nurdin

A Computer Science Student at Gunadarma University