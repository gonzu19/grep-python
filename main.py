import os
import sys
from termcolor import colored

def highlight_word(sentence, word):
    # Split the sentence using the word as delimiter
    parts = sentence.split(word)

    # Join the parts, coloring the word to highlight
    highlighted_sentence = colored(word, 'red').join(parts)

    return highlighted_sentence

# Function to list all files recursively
def list_files_in_directory(directory=os.getcwd()):
    all_files = []
    for root, directories, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)
    return all_files

def grep(file:str,sequence:str):
    """Función que imita el comportamiento de grep"""
    if sys.stdin.isatty():
        with open(file,"r") as archivo:
            contenido = archivo.read()
            if sequence not in contenido:
                return None
            print(f"------------------\nfile: {file}\n------------------")
            contenido_separado_por_lineas = contenido.split('\n')
            #contenido_separado_por_espacios = contenido.split(' ')
            for linea in contenido_separado_por_lineas:
                if sequence not in linea:
                    pass
                else:
                    colored_text = highlight_word(sentence=linea,word=sequence)
                    print(colored_text)
    else:
        for line in sys.stdin:
            if sequence not in line:
                pass
            else:
                colored_text = highlight_word(sentence=line.strip(),word=sequence)
                print(colored_text)
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one additional argument.")
        print("Usage: python {} <additional_argument>".format(sys.argv[0]))
        sys.exit(1)
    files = list_files_in_directory()
    for file in files:
        try:
            if ".git" not in file:
                grep(file=file,sequence=sys.argv[1])
        except Exception as e:
            print(f"Exception: {e}")
        
        
