import utils
import codecs
import os
from subprocess import call
word = 'abacate'
sentence = 'abc def ghi asdasd abc akakaka 12321321 11 98'
chars = utils.get_chars(word)

print(utils.sort(utils.get_chars(word)))
print(utils.sort(sentence))

def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')
      
def help(args):
    print("\nclassify, c : Classifica uma lista de elementos\n    -f [<caminho do arquivo .txt>] : Usa entrada por arquivo em vez de manual (default)\n    --dedupe : Desduplica os itens da lista\n    --invert : Inverte a classificação (ordem decrescente ou alfabética invertida)\n    --no-numbers : Excluí todos os números de uma lista\n    -s [<caminho do arquivo para salvar>]: Salva a lista classificada\nexit : Sai do programa\n")

def classify(args):
    sentence = ''
    manual = True
    dedupe = False
    numbers = True
    invert = False
    savePath = ''
    filePath = ''

    if args.count('-f') != 0 :
        filePath = args[args.index('-f')+1]
        manual = False
        text = codecs.open(r'{}'.format(filePath), "r+", 'utf8')
        sentence = text.read()
        text.close()

    if manual == True:
        sentence = input("Input items: \n\n>")

    if  args.count('--no-numbers') != 0:
        numbers = False

    if  args.count('--dedupe') != 0:
        dedupe = True
    
    sorted_sentence = utils.sort(sentence, dedupe=dedupe, numbers=numbers)


    if args.count('-s') != 0:
        savePath = args[args.index('-s')+1]

    if  args.count('--invert') != 0:
        invert = True

    print(sorted_sentence)

def run():
    while(True):
        args = input("$ Enter command\n\n>").split()
        try:
            command = args[0]
            args.pop(0)
        except Exception:
            print("You must enter a command!")
            break
        
        globals()[command](args)
        # try:
        #     globals()[command](args)
        # except Exception:
        #     print("This command doesn't exist. Use 'help' for more information!")



while(True):
    run()