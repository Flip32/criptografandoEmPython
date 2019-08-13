from random import randint
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'w', 'z', ' ']
#key = 'CHAVECRIPTO'
key = ''
#msg = 'HELLO WORLD'
print('O Programa retornará sua msg em maíusculas.')
msg = str(input('Digite a msg a ser criptografada: ')).upper()
criptKey = []
msgInNumber = []
somaCritp = []
subtracao = []
msgCript = []
msgCriptografada = ''
msgDescript = []
msgDescriptografada = ''
arrRandom = []

print('TEXTO LIMPO: ', msg)

#Criando a Chave aleatoriamente!
while len(arrRandom) <= (len(msg) - 1):
    nRandom = randint(0, 25)
    arrRandom.append(alfabeto[nRandom])
key = ''.join(arrRandom)
print('CHAVE GERADA: ', key)


def criptografando(chave, mensagem):
    for key in chave:
        criptKey.append(alfabeto.index(key.lower()))
    for letra in mensagem:
       msgInNumber.append(alfabeto.index(letra.lower()))
    #print('chave transformada em numeros', criptKey)
    #print('msg transformada em numeros  ', msgInNumber)
    i = 0
    while i < len(chave):
        soma = criptKey[i] + msgInNumber[i]
        if soma >= 27:
            soma -= 27
        somaCritp.append(soma)
        i += 1
    #print('soma = Chave + Msg            ', somaCritp)
    for n in somaCritp:
        msgCript.append(alfabeto[n].upper())
    msgCriptografada = ''.join(msgCript)
    print('TEXTO CRIPTOGRAFADO: ', msgCriptografada)


criptografando(key, msg)


def desCritografando(chave, msgC):
    f = 0
    while f < len(chave):
        sub = msgC[f] - chave[f]
        if sub < 0:
            sub += 27
        subtracao.append(sub)
        f += 1
    #print('subtração = Mensagem Critografada - Chave', subtracao)
    for m in subtracao:
        msgDescript.append(alfabeto[m].upper())
        msgDescriptografada = ''.join(msgDescript)
    print('MENSAGEM DESCRIPTOGRAFADA: ', msgDescriptografada)


desCritografando(criptKey, somaCritp)