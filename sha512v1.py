#-*- encoding: utf-8
import crypt
def testPass(cryptPass):
    salt=cryptPass.split('$')[2]
    print ('[i] salt = ' + salt)
    myPass=cryptPass.split('$')[3]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, '$6$' + salt + '$')
        cryptWord = cryptWord.split('$')[3]
        if cryptWord==myPass:
            print ('[+] Found password: ' + word + '\n')
            return
        print ('[-] Password not found.\n')
        return

def main():
    passFile = open('shadow.txt','r')
    for line in passFile.readlines():
        if ':' in line:
            user=line.split(':')[0]
            cryptPass=line.split(':')[1].strip(' ')
        if len(cryptPass)>1:
            print ('[*] Cracking password for: ' + user)
            testPass(cryptPass)
if __name__ == '__main__':
    main()
