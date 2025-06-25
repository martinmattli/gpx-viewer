import os
import zipfile
import gzip
import shutil
from fitparse import FitFile
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

input_folder = "gpx_files"
output_folder = "gpx_files"

def convert_fit_to_gpx(fit_path, gpx_path):
    fitfile = FitFile(fit_path)
    gpx = Element('gpx', attrib={
        'creator': 'fitparse',
        'version': '1.1',
        'xmlns': 'http://www.topografix.com/GPX/1/1'
    })
    trk = SubElement(gpx, 'trk')
    trkseg = SubElement(trk, 'trkseg')

    try:
        for record in fitfile.get_messages("record"):
            lat = None
            lon = None
            for d in record:
                if d.name == "position_lat":
                    lat = d.value * (180 / 2**31)
                if d.name == "position_long":
                    lon = d.value * (180 / 2**31)
            if lat and lon:
                pt = SubElement(trkseg, 'trkpt', lat=str(lat), lon=str(lon))

        xml_str = parseString(tostring(gpx)).toprettyxml(indent="  ")
        with open(gpx_path, "w") as f:
            f.write(xml_str)
        print(f"✅ Konvertiert: {fit_path} → {gpx_path}")
    except Exception as e:
        print(f"⚠️ Fehler bei {fit_path}: {e}")

# Dateien im Eingabeordner verarbeiten
for fname in os.listdir(input_folder):
    path = os.path.join(input_folder, fname)
    if fname.endswith(".zip"):
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(input_folder)
            print(f"📦 Entpackt: {fname}")
    elif fname.endswith(".fit.gz"):
        # .fit.gz entpacken
        fit_name = fname[:-3]  # Entfernt .gz
        fit_path = os.path.join(input_folder, fit_name)
        with gzip.open(path, 'rb') as f_in:
            with open(fit_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"🗜️ Entpackt .fit.gz: {fname} → {fit_name}")
        gpx_name = fit_name.replace(".fit", ".gpx")
        gpx_path = os.path.join(output_folder, gpx_name)
        convert_fit_to_gpx(fit_path, gpx_path)
    elif fname.endswith(".fit"):
        gpx_name = fname.replace(".fit", ".gpx")
        gpx_path = os.path.join(output_folder, gpx_name)
        convert_fit_to_gpx(path, gpx_path)
