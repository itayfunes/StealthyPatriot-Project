# When using, please edit line 10 ("YOURFILE.py"), change it to your file name!
import sys
from cx_Freeze import setup, Executable
build_exe_options = {"includes": ["PIL"]}
setup(
    name = "VMware, Inc.",
    version = "1.166.57",
    description = "VMware Tool",
    options = {"build_exe": build_exe_options},
    executables = [Executable("mal.py", base="Win32GUI")] # CHANGE THIS "YOURFILE.py" TO YOUR FILE NAME !
)