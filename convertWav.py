import sys
import execute
import wavConverter

def main():
    print(sys.argv)

    if sys.argv[1] == '-w' or sys.argv[1] == '--wav':
        with open(sys.argv[2], 'rb') as binary:
            fileName = binary.name
            fileName = fileName.split('.exe')[0]
            binary = binary.read()
            wavConverter.convertBinaryToWav(''.join(fileName), binary)
    if sys.argv[1] == '-e' or sys.argv[1] == '--execute':
            convertedBinary = wavConverter.convertWavToBinary(sys.argv[2])
            execute.executeBinary(convertedBinary)
            
if __name__ == '__main__':
    main()




