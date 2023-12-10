# Import Statements
import os, shutil
from io import TextIOWrapper
from typing import Final
from zipfile import ZipFile
from urllib.request import urlretrieve

# File Docstring
# Rico App Kit || build.py
# ------------------------
# "Builds" a .zip file that bundles the 
# MaxTime JRE, .jar file, and custom .bat script
#
# @author https://github.com/MaxineToTheStars

# Enums

# Interfaces

# Constants
CONSTANT_VERSION_STRING: Final[str] = "v1.0.0"
CONSTANT_MAXTIME_JRE_DOWNLOAD_URL: Final[str] = "https://github.com/MaxineToTheStars/MaxTime-JRE/releases/download/latest/maxtime-jre.zip"
CONSTANT_CUSTOM_BAT_DATA: Final[str] = """
@echo off
echo Rico App Kit Version: RAC-v1.0.0
echo JRE Supplied: MaxTime JRE v2.0.0 for Java v11
echo https://github.com/MaxineToTheStars/MaxTime-JRE
echo -----------------------------------------------
.\\maxtime-jre\\bin\\java.exe -jar app.jar 
"""

# Public Variables

# Private Variables

# main()
def main() -> None:
	# Show welcome message
	_show_welcome_message()

	# Download MaxTime JRE
	_download_maxtime_jre()

	# Build .zip
	_build_zip()

# Public Methods

# Private Methods
def _show_welcome_message() -> None:
	"""
	Shows the welcome message
	
	@return void
	"""
	print(f"Rico App Kit - {CONSTANT_VERSION_STRING}")
	print("https://github.com/MaxineToTheStars/Rico-App-Kit")
	print("------------------------------------------------\n")

def _download_maxtime_jre() -> None:
	"""
	Downloads the latest release of the MaxTime JRE (Windows)

	@return void
	"""
	# Show downloading JRE message
	print("[DOWNLOAD - MaxTime JRE] Downloading latest Windows JRE...")

	# Download JRE
	urlretrieve(CONSTANT_MAXTIME_JRE_DOWNLOAD_URL, "./maxtime-jre.zip")

	# Show extracting JRE message
	print("[DOWNLOAD - MaxTime JRE] Extracting MaxTime JRE...")

	# Extract the .zip file to ./dist directory
	maxtimeJREZip: ZipFile = ZipFile("./maxtime-jre.zip", "r")
	maxtimeJREZip.extractall("./dist/maxtime-jre")

	# Show clean up message
	print("[DOWNLOAD - MaxTime JRE] Cleaning up workspace...")

	# Clean up
	os.remove("./maxtime-jre.zip")

	# Show done message
	print("[DOWNLOAD - MaxTime JRE] Done!")

def _build_zip() -> None:
	"""
	Builds the given zip file

	@return void
	"""
	# Show building message
	print("[BUILD] Preparing for build...")

	# Create .bat file
	launchBat: TextIOWrapper = open("./dist/run.bat", "a+")
	launchBat.writelines(CONSTANT_CUSTOM_BAT_DATA)
	launchBat.close()

	# Move the .jar
	shutil.copyfile("./src/app.jar", "./dist/app.jar")

	# Show build done message
	print("[BUILD] Done!")

# Run
if __name__ == "__main__":
	main()