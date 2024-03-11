from PyPDF2 import PdfReader


def ExtImagenesPDF(ruta,hoja):
    """"Extrae las imagenes de un pdf dadas las hojas y la ruta del archivo con su nombre completo
    
    Args:
        [parametro1]: (str) | "./dir/name.pdf" | "name.pdf" 
        [parametro1]: (str) | "./dir/name.pdf" | "name.pdf" 
         

    Returns:
        Un obj. de tipo imagen
    """

    reader=PdfReader(ruta)
    page=reader.pages[hoja-1]
    cont_img=0
    for imgObj in page.images:
        with open('./imagenes/'+str(cont_img)+'-'+imgObj.name,"wb") as img:
            img.write(imgObj.data)
        cont_img+=1



# ExtImagenesPDF("ppto. PRECCE GABRIELA 16.11.23.pdf", 1)
