import cx_Freeze
import os.path


# python3 setup.py build
# python3 setup.py bdist_msi

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("pygameTest.py")]



cx_Freeze.setup(
	name = "Slither",
	options = {"build_exe":{"packages":["pygame"], "include_files":["apple.png", "snake.png"]}}, 
	description = "Slither Game Tutorial",
	executables = executables
	)