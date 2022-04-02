import os
import subprocess
import sys

if sys.platform == 'win32':
    args = '"C:\\\\Program Files\\\\gs\\\\gs9.23\\\\bin\\\\gswin64c" ' \
           '-sDEVICE=mswinpr2 ' \
           '-dBATCH ' \
           '-dNOPAUSE ' \
           '-dFitPage ' \
           '-sOutputFile="%printer%myPrinterName" '
    ghostscript = args + os.path.join(os.getcwd(), 'example.pdf').replace('\\', '\\\\')
    subprocess.call(ghostscript, shell=True)