import pdfquery
from lxml import etree
from bs4 import BeautifulSoup
import re

pdf_path="stm22.pdf"
pdf=pdfquery.PDFQuery(pdf_path)
pdf.load()
page_count=len(pdf._pages)


#print (pdf_tree)

def coloumn_assign(x0,x1):
    #print (float(x0))
    if float(x0)>46 and float(x0)<48:
        return "date"
    if float(x1)>355 and float (x1)<357:
        return "withdrawl"
    if float(x1)>448 and float (x1)<449:
        return "deposit"
    if float(x1)>555.5 and float (x1)<556.5:
        return "c_bal"
    if float(x0)>95.5 and float (x0)<96.5:
        return "remark"
    return "none"

for page in range(1,page_count):
    pdf.load(page)
    pdf_tree=''
    table_data={}
    pdf_tree=etree.tounicode(pdf.tree)
    res=BeautifulSoup(pdf_tree,features='lxml').findAll('lttextboxhorizontal')
    for tag in res:
        x0=tag.get('x0')
        x1=tag.get('x1')
        coloumn=coloumn_assign(x0,x1)
        if re.match('none',coloumn):
            pass
        else:
            y0 = tag.get('y0')
            if (y0 in table_data):
                table_data[y0][coloumn]=tag.get_text()
            else:
                table_data[y0]={}
                table_data[y0][coloumn] = tag.get_text()
            #print ("page:"+str(page)+"\t"+str(y0)+"\t"+coloumn+"\t"+tag.get_text())
    keydel=[]
    for y0 in table_data:
        if ('date' in table_data[y0]):
            pass
        else:
            keydel.append(y0)
    for key in keydel:
        del table_data[key]

    print ("page"+str(page)+"\n")
    print(table_data)