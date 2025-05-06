# command interpreter in python
import shutil
import os
import cmd
import platform

class MyCommand(cmd.Cmd):
	prompt = "(mycommand) > "

	def do_quit(self, arg):
		"""This quits or exits the program."""
		return True
	
	def do_cd(self, path):
		"""This changes the current working directory."""
		if not path:
            		print("Usage: cd <path>")
            		return
		try:
			os.chdir(path)
			print(f"Changed directory to {os.getcwd()}")
		except FileNotFoundError:
			print(f"No such directory found: {path}")
		except Exception as e:
			print(f"Error: {e}")

	def do_ls(self, arg):
		"""This lists the files and directories in the current working directory."""
		try:
			for entry in os.listdir():
				print(entry)
		except Exception as e:
			print(f"Error: {e}")

	def do_pwd(self, arg):
		"""This prints the current working directory."""
		print(os.getcwd())

	def do_clear(self, arg):
		"""This clears the screen."""
		os.system("cls" if platform.system() == "Windows" else "clear")

	def do_rm(self, file):
		"""This removes a file."""
		if not file:
			return
		try:
			if os.path.isfile(file):
				os.remove(file)
				print(f"Removed file: {file}")
			else:
				print(f"No such file found: {file}")
		except Exception as e:
			print(f"Error removing file: {e}")

	def do_mv(self, arg):
		"""This moves a file or directory."""
		try:
			src, dest = arg.split()
			
			if not os.path.exists(src):
				print(f"Error: '{src}' does not exist.")
				return
			
			shutil.move(src, dest)
			print(f"Moved from '{src}' to '{dest}'")
		except ValueError:
			print("Error: Both source and destination not given.")
		except Exception as e:
			print(f"Error: {str(e)}")

	def do_cp(self, arg):
		"""This copies a file or directory."""
		try:
			src, dest = arg.split()

			if not os.path.exists(src):
				print(f"Error: '{src}' does not exist.")
				return

			if os.path.isdir(src):
				shutil.copytree(src, dest)
			else:
				shutil.copy2(src, dest)

			print(f"Copied from '{src}' to '{dest}'")
		except ValueError:
			print("Error: Both source and destination not given.")
		except Exception as e:
			print(f"Error: {str(e)}")
	
	#aliasing
	do_exit = do_quit
	do_dir = do_ls

MyCommand().cmdloop()
