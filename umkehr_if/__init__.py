import os.path
import os
from .umkehr_if import set_umkehr_inputfolder

inputfolder,name = os.path.split( __file__)
datafolder = inputfolder + os.sep
print('Umkehr_IF, __init__ Setting data folder to ',datafolder,' from file variable ', __file__)
set_umkehr_inputfolder( datafolder )


