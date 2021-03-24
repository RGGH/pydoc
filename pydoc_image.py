
from docxtpl import DocxTemplate
import os

image_dir = 'templates/images/'
files = [ f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir,f)) ]


tpl = DocxTemplate('templates/replace_picture_tpl.docx')

for file in files:

        DEST_FILE = f'output/auto_{file.rsplit(".",1)[0]}.docx'

        context = {}


        old_im = "fruit_logo.png"
        new_im = f"templates/images/{file}"

        tpl.replace_pic(old_im, new_im)
        tpl.render(context)
        tpl.save(DEST_FILE)
