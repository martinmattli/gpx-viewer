# 🚴 GPX Viewer & FIT-Konverter

Ein kleines Streamlit-Tool zur Anzeige von GPX-Routen (z.B. aus Strava) auf einer interaktiven Karte – plus Konverter für `.fit(.gz)` → `.gpx`.

## 📦 Features

- Lädt und visualisiert beliebig viele GPX-Dateien
- Nutzt `folium` für Kartenanzeige in Streamlit
- Optionaler Konverter von `.fit` oder `.fit.gz` zu `.gpx`

### 📤 Alle Strava-Aktivitäten exportieren

1. Logge dich bei [Strava ein](https://www.strava.com/settings/profile)
2. Gehe zu Settings → „My Account“
3. Starte den Export unter „Download or Delete Your Account“ → „Get started“
4. Lade das Archiv herunter und entpacke es
5. Importiere die `.fit.gz`-Dateien in dieses Tool


## ▶️ Lokales Setup

```bash
pip install -r requirements.txt
streamlit run gpx_viewer.py
