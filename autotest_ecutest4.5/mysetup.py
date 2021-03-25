#my setup.py
from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

py2exe_options={
      "includes":["sip"],
      "dll_excludes":["MSVCP90.dll",],
      "compressed":1,
      "optimize":2,
      "ascii":0,
      "bundle_files":3,
      }
setup(
      name = 'Auto Create',
      version = '1.0',
      windows = [{'script':'AutoCreate 4.5.py','icon_resources':[(1,'timgCADXKVUY.ico')]}],
      #zipfile = None,
      options = {'py2exe':py2exe_options}
      )
#distutils.core.setup(windows=[{'script':'MainCreate.py','icon_resources':[(1,'timgCADXKVUY.ico')]}])

