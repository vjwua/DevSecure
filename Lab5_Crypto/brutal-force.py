phrase = 'vppanlwxlyopyncjae'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
codeword = 'codeword.txt'

def newlineremover(filename):
    return ''.join(open(filename).read().split('\n'))

def brutalforce(message, letters):
    for key in range(len(letters)):
        translated = ''
        for symbol in message:
            if symbol in letters:
                num = letters.find(symbol)
                num -= key
                if num < 0:
                    num += len(letters)
                translated += letters[num]
            else:
                translated += symbol
        print('Key #%s: %s' % (key, translated))
        if translated == newlineremover(codeword):
            print('Codeword is found')
            break

brutalforce(phrase, alphabet)
