# input_oracion = "el niño llora"
# frase = input_oracion.split()
sintaxis = {}

# formula = S{SN{Art, Sust}, SV{V, Adj}}

SN = ["art","sust"]
SV = ["v","adj"]
formula = [SN,SV]

def analisi_sintactico(formula,frase):
    bandera = 0
    try:
        for index,S in enumerate(formula):
            for indice,palabra in enumerate(S):
                sintaxis[formula[index][indice]] = frase[bandera]
                bandera = bandera + 1

    except IndexError:
        sintaxis[formula[index][indice]] = None

    return sintaxis
