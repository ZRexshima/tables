from fpdf import FPDF
from fpdf.fonts import FontFace

pdf = FPDF()
pdf.set_font("Helvetica")
pdf.set_display_mode(zoom="fullwidth")

TABLE_DATA = (
    ("First name", "Last name", "Age", "City"),
    ( "Jules", "Smith", "34", "San Juan"),
    ( "Mary", "Ramos", "45", "Orlando"),
    ("Carlson", "Banks", "19", "Los Angeles"),
    ("Lucas", "Cimon", "31", "Saint-Mathurin-sur-Loire"),
)

blue = (0, 0, 255)
grey = (128, 128, 128)
headings_style = FontFace(emphasis="ITALICS", color=blue, fill_color=grey)
pdf.add_page()
pdf.set_font("Times", size=16)
with pdf.table(headings_style=headings_style) as table:
    for data_row in TABLE_DATA:
        row = table.row()
        for datum in data_row:
            row.cell(datum)
pdf.output("styled-headers-table.pdf")
