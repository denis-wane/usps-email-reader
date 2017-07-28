'''
Created on Jul 28, 2017

@author: denis.r.wane
'''
import sys
from cx_Freeze import setup, Executable

base = None

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","sys","email","imaplib","configparser"], "excludes": ["tkinter"]}

executables = [Executable("email_reader.py", base=base)]

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "email_reader",
    options = {"build_exe": build_exe_options},
    version = "1.0",
    description = 'IDID Email Reader',
    executables = executables
)