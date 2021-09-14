# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['E:/CineBook/login.py'],
             pathex=['E:\\CineBook'],
             binaries=[],
             datas=[('E:/CineBook/admin.py', '.'), ('E:/CineBook/admin_login.py', '.'), ('E:/CineBook/boomika.py', '.'), ('E:/CineBook/cruella.py', '.'), ('E:/CineBook/data.json', '.'), ('E:/CineBook/home.py', '.'), ('E:/CineBook/json_db.py', '.'), ('E:/CineBook/login.py', '.'), ('E:/CineBook/mask.py', '.'), ('E:/CineBook/mimi.py', '.'), ('E:/CineBook/mod_data.py', '.'), ('E:/CineBook/register.py', '.'), ('E:/CineBook/shershaah.py', '.'), ('E:/CineBook/asserts', 'asserts/')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='login',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='E:\\CineBook\\asserts\\icons\\clapperboard.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='login')
