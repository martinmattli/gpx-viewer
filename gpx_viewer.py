import streamlit as st
import gpxpy
import folium
from streamlit_folium import st_folium
import os
import io

# GPX-Dateien parsen
def parse_gpx_stream(file_stream):
    gpx = gpxpy.parse(file_stream)
    coords = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                coords.append((point.latitude, point.longitude))
    return coords

st.title("🚴‍♂️ Alle Strava GPX-Routen anzeigen")

# Option 1: GPX-Dateien per Upload
uploaded_files = st.file_uploader(
    "GPX-Dateien hochladen", type="gpx", accept_multiple_files=True
)

all_coords = []

if uploaded_files:
    for uploaded_file in uploaded_files:
        coords = parse_gpx_stream(io.StringIO(uploaded_file.getvalue().decode("utf-8")))
        if coords:
            all_coords.append((uploaded_file.name, coords))
    st.success(f"{len(all_coords)} Datei(en) via Upload geladen.")

# Option 2: Lokaler Ordner (nur lokal verwendbar)
gpx_folder = "gpx_files"
if os.path.exists(gpx_folder):
    local_files = [f for f in os.listdir(gpx_folder) if f.endswith(".gpx")]
    for file in local_files:
        with open(os.path.join(gpx_folder, file), "r", encoding="utf-8") as f:
            coords = parse_gpx_stream(f)
            if coords:
                all_coords.append((file, coords))
    if local_files:
        st.info(f"{len(local_files)} lokale Datei(en) geladen.")
else:
    st.warning(f"Ordner '{gpx_folder}' nicht vorhanden (nur für lokale Nutzung relevant).")

# Karte anzeigen
if all_coords:
    center = all_coords[0][1][len(all_coords[0][1]) // 2]
    m = folium.Map(location=center, zoom_start=12)

    for filename, coords in all_coords:
        folium.PolyLine(coords, color="blue", weight=3, tooltip=filename).add_to(m)

    st_folium(m, width=800, height=600)
else:
    st.info("Keine GPX-Daten verfügbar.")
