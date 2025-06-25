import streamlit as st
import gpxpy
import folium
from streamlit_folium import st_folium
import os

# GPX-Dateien parsen
def parse_gpx_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        gpx = gpxpy.parse(f)
        coords = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    coords.append((point.latitude, point.longitude))
        return coords

# App-UI
st.title("🚴‍♂️ Alle Strava GPX-Routen anzeigen")

# Ordnerpfad anpassen
gpx_folder = "gpx_files"

if not os.path.exists(gpx_folder):
    st.error(f"Ordner '{gpx_folder}' nicht gefunden. Lege ihn im Projektordner an und füge GPX-Dateien hinzu.")
else:
    files = [f for f in os.listdir(gpx_folder) if f.endswith(".gpx")]
    if not files:
        st.warning("Keine GPX-Dateien im Ordner gefunden.")
    else:
        all_coords = []
        for file in files:
            filepath = os.path.join(gpx_folder, file)
            coords = parse_gpx_file(filepath)
            if coords:
                all_coords.append((file, coords))

        # Karte zentrieren auf erste Route
        if all_coords:
            center = all_coords[0][1][len(all_coords[0][1]) // 2]
            m = folium.Map(location=center, zoom_start=12)

            # Routen hinzufügen
            for filename, coords in all_coords:
                folium.PolyLine(coords, color="red", weight=3, tooltip=filename).add_to(m)

            st.success(f"{len(all_coords)} GPX-Dateien geladen.")
            st_folium(m, width=800, height=600)
