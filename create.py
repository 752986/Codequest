import sys
import os
import shutil
from urllib import request
import zipfile

# check for correct argument format
if len(sys.argv) == 1:
	print("Put the problem name (taken from its URL) after the command.\nExample: `python create.py hello-world`")
	exit()
elif len(sys.argv) > 2:
	print("Don't include spaces in the problem name. It should be formatted like in its URL.")
	exit()

problem = sys.argv[1]
formatted = problem.replace("-", "_")

# don't overwrite existing files
if os.path.isdir(formatted):
	print(f"The folder `{problem}` already exists.")
	exit()

# create folder and copy template
os.mkdir(formatted)
shutil.copy("template.py", f"{formatted}/{formatted}.py")

# fetch files from internet
request.urlretrieve(f"https://lmcodequestacademy.com/api/static/problems/{problem}", f"{formatted}/{formatted}.pdf")
request.urlretrieve(f"https://lmcodequestacademy.com/api/static/samples/{problem}", f"{formatted}/{formatted}_temp.zip")

# unzip input
with zipfile.ZipFile(f"{formatted}/{formatted}_temp.zip") as zipped:
	with zipped.open("1.in") as data:
		with open(f"{formatted}/input.txt", "wb") as input_file:
			input_file.write(data.read())

# remove temporary zip file
os.remove(f"{formatted}/{formatted}_temp.zip")
