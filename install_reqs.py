import subprocess
import sys
import os

required_packages = []

# Extract package names from files
for filename in ['database.py', 'note.py', 'note_taking_app.py', 'run.py']:
    with open(filename) as f:
        for line in f:
            if line.startswith('import'):
                package_name = line.split()[1]
                if ',' in package_name:
                    package_name = package_name.split(',')[0]
                required_packages.append(package_name)

# Remove duplicates
required_packages = list(set(required_packages))

# Activate virtual environment
venv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'myenv'))
if sys.platform == 'win32':
    activate_path = os.path.join(venv_path, 'Scripts', 'activate.bat')
else:
    activate_path = os.path.join(venv_path, 'bin', 'activate')
subprocess.call(['source', activate_path], shell=True)

# Install missing packages
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call(['pip', 'install', package])

