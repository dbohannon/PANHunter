from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"]}

setup(
	name = "PAN Hunter",
	version = "1.0", 
	description = "Locates all personal account numbers (PAN) within specified files.", 
	author = "David A. Bohannon",
	executables = [Executable(script = "exec_pan_hunter.py", targetName="PAN_Hunter", icon="crosshairs.ico")]
)

