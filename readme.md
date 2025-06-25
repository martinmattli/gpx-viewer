# 🚴 GPX Viewer & FIT-Konverter

Ein kleines Streamlit-Tool zur Anzeige von GPX-Routen (z. B. aus Strava) auf einer interaktiven Karte – plus Konverter für `.fit(.gz)` → `.gpx`.

## 📦 Features

- Lädt und visualisiert beliebig viele GPX-Dateien
- Nutzt `folium` für Kartenanzeige in Streamlit
- Optionaler Konverter von `.fit` oder `.fit.gz` zu `.gpx`

## ▶️ Lokales Setup

```bash
pip install -r requirements.txt
streamlit run gpx_viewer.py
