def letter_ascii(message):
    message_ascii = ""
    for i in message:
        for letter in i:
            aux = str(ord(letter))
            if len(aux)==2:
                message_ascii = message_ascii + aux  + "00"
            elif len(aux)==1:
                message_ascii =  message_ascii +  aux  + "00"
            else:
             message_ascii = message_ascii + aux + "00"
    message_ascii = int(message_ascii)
    return message_ascii

def ascii_letter(message_ascii):
    ascii = str(message_ascii)
    message = ""
    text = []
    aux = ""
    for i in range(0, len(ascii)):
        if ascii[i] != "0" :
            aux = aux + ascii[i]
        elif ascii[i] == "0" and i == (len(ascii) - 1):
            continue
        elif ascii[i] == "0" and ascii[i - 1] != "0" and ascii[i + 1] != "0":
            aux = aux + ascii[i]
        elif ascii[i] == "0" and ascii[i + 1] == "0" and i == (len(ascii) - 2):
            text.append(aux)
            aux = ""
        elif ascii[i] == "0" and ascii[i + 1] == "0" and ascii[i + 2] != "0" and i != (len(ascii) - 1):
            text.append(aux)
            aux = ""
        elif ascii[i] == "0" and ascii[i + 1] == "0" and ascii[i + 2] == "0":
            aux = aux + ascii[i]
    
    for i in text:
        message = message + chr(int(i))

    return message
def el_gamal_gen_llave_publica(d, alpha, p):
    beta = (alpha**d)%p

    return (beta, p, alpha)

def el_gamal_encrip(x, llave_publica):

    beta = llave_publica[0]
    p = llave_publica[1]
    alpha = llave_publica[2]
    
    #Se selecciona el i para hacer las operaciones
    i = int(input("Ingrese un numero entre 2 y el primo para que sea el i: "))
    while (True):
        if i==1 or i==(p-1) or i>=p:
            print("Numero invalido")
            i = int(input("Ingrese un numero entre 2 y " + str(p-1) + " para que sea el i: "))
        else:
            break

    KE = (alpha**i)%p


    #se cifra el mensaje
    N2 = (x*(beta**i))%p

    return (N2, KE)

def el_gamal_decrip(texto_cifrado, p, d):

    KE = texto_cifrado[1]
    N2= texto_cifrado[0]
    #Se descifra utilizando KE y la optimizacion del pequeño teorema de fermat

    x = (KE**d)%p
    y=pow(x, -1, p)
    texto_claro=(N2*y)%p

    return texto_claro

def firma(texto,llave_publica,privada):
    p = llave_publica[1]
    alpha = llave_publica[2]
    e=p-1
    H=37
    Hi=pow(H, -1, e)
    r=pow(alpha,H,p)
    s=((texto-(privada*r))*Hi)%(e)
    return (r,s)
def comprobacion_firma(firma,llave_publica,texto_claro):
    r=firma[0]
    s=firma[1]
    beta = llave_publica[0]
    p = llave_publica[1]
    alpha = llave_publica[2]
    N=pow(r,s,p)
    N2=pow(beta,r,p)
    K=(N*N2)%p  
    koriginal=pow(alpha,texto_claro,p)

    if K==koriginal:
        print ("si es la firma :D")
    else:
        print("No es la firma")
def main():
    

    pbob = 149266604066765214257465899845052595936980433085281120472438633560109109845062080813195674897136525949840184965312505298869948722977649469023084361550412989486060207917580540454081140587353862234445577520476872543676486167892443872308705026778461121261224322495328346630383486386663628878772838449087770123303
    alpha_bob = 7
    priv_bob = 21702
    priv_alice=12154
    alpha_alice =1513
    palice=116136133237524628623079973436761666157812135802554422133884399716278215827708188540430994158743163224360474004390260851035079396569070805436204141716645377206469931168305351122258807934047024235765278566582937247825531441295648260124631056178986340098086793666788683120626019654875802245983332214723863553333
    pub_bob = el_gamal_gen_llave_publica(priv_bob, alpha_bob, pbob)
    pub_alice = el_gamal_gen_llave_publica(priv_alice,alpha_alice, palice)
    mensajetexto="hola"
    mensaje=letter_ascii(mensajetexto)
    print(mensaje)
    x=firma(mensaje,pub_alice,priv_alice)
    

 
    texto_cifrado = el_gamal_encrip(mensaje, pub_bob)
    print("texto cifrado: " +str(texto_cifrado))
    texto_claro = el_gamal_decrip(texto_cifrado, pbob, priv_bob)
    print(texto_claro)
    print("texto claro: " +ascii_letter(str(texto_claro)))
    comprobacion_firma(x, pub_alice,texto_claro)

   
main()