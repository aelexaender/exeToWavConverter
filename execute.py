import subprocess
import tempfile

def executeBinary(binary):
    with tempfile.NamedTemporaryFile(delete=False) as tempFile:
        tempFile.write(binary)
        tempFilePath = tempFile.name

    subprocess.call([tempFilePath])