import os
from pathlib import Path
import zipfile
import requests
import pandas as pd

# Función para descargar y descomprimir archivos ZIP
def unzip(zipfilename, xslx_dir):
    print(f"Descomprimiendo {zipfilename}...")
    with zipfile.ZipFile(zipfilename, 'r') as zip_ref:
        zip_ref.extractall(xslx_dir)

def process_xslx(xslx_file):
    print(f"Processing {xslx_file}")
    call_names = {
        '02': 'Congreso',
        '07': 'Europa',
    }
    call = call_names[xslx_file.stem[len("PROV_"):len("PROV_02")]]
    year = xslx_file.stem[len("PROV_02_"):len("PROV_02_2000")]
    month = xslx_file.stem[len("PROV_02_2000"):len("PROV_02_200012")]
    print(f"***** {call} {year} {month}")
    import openpyxl
    excel = openpyxl.load_workbook(xslx_file).active

    full_name_row = 3
    acronym_row = 4
    first_district_row = 6
    if year < "2015":
        census_col = 5
        voters_col = 6
        valid_col = 7
        blank_col = 9
        null_col = 10
        first_party_col = 11
    else:
        # CERA changed data order
        census_col = 7
        voters_col = 11
        valid_col = 12
        null_col = 14
        blank_col = 15
        first_party_col = 16
    
    data = [
        [value for value in row]
        for row in excel.values
    ]
    provinces = dict(
        (row[1], first_district_row+i)
        for i, row in enumerate(data[first_district_row:])
        if row[1] is not None
    )
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    for province, province_idx in provinces.items():
        selected_data = data[province_idx]
        province_code = selected_data[1]
        province_name = selected_data[2].strip().split('/')[0].strip()
        if province_name == "Total" : continue
        output_file = output_dir/f"{year}-{month:02}-{call}-{province_code:02}-{province_name}.tsv"
        party_cols = [
            dict(
                col = i,
                acronym = acronym,
                name = name,
            )
            for i, (name, acronym) in enumerate(zip(data[full_name_row], data[acronym_row]))
            if name is not None
        ]

        seats= sum((x for x in selected_data[first_party_col+1::2] if x is not None))
        result = [
            [ "Siglas", "Votos", "Diputados", "Candidatura",],
            [ "censo",  selected_data[census_col], seats, None,],
            [ "participacion", selected_data[voters_col], None, None],
            [ "abstencion", selected_data[census_col] - selected_data[voters_col], None, None],
            [ "nulos", selected_data[null_col], None, None],
            [ "blancos", selected_data[blank_col], None, None],
        ] + [
            [
                party['acronym'],
                selected_data[party['col']],
                selected_data[party['col']+1],
                party['name'],
            ]
            for party in party_cols
            if selected_data[party['col']]
        ]
        #print("="*50)
        #print(result)
        content = '\n'.join([
            '\t'.join([
                str(cell).strip() if cell is not None else ""
                for cell in row
            ])
            for row in result
        ])
        print(f"== {output_file}")
        print(content)
        output_file.write_text(content)



# URL del archivo ZIP con los resultados de las elecciones generales
url = 'https://infoelectoral.interior.gob.es/downloads/elecciones_generales_2023.zip'

# Carpeta donde se almacenarán los archivos descargados y descomprimidos
xslx_dir = 'xslx_files'

# Crear la carpeta si no existe
os.makedirs(xslx_dir, exist_ok=True)

for zipped in Path().glob("*.zip"):
    unzip(str(zipped), xslx_dir)

for xslx_file in Path(xslx_dir).glob("PROV_02*.xlsx"):
    process_xslx(xslx_file)


