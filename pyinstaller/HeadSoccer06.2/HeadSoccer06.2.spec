# -*- mode: python -*-

block_cipher = None


a = Analysis(['/home/newtonis/Dropbox/Proyectos2015/HeadSoccer/head_soccer_06_2/main.py'],
             pathex=['/home/newtonis/Dropbox/Proyectos2015/HeadSoccer/pyinstaller/HeadSoccer06.2'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
pyz = PYZ(a.pure,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='HeadSoccer06.2',
          debug=False,
          strip=None,
          upx=True,
          console=True )
