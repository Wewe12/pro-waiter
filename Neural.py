import numpy as np

#funkcja aktywacji (sigmoida)
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
#normalizacja wejscia
def normalize(array):
    for i in range (3):
        if (i == 0):
            array[i] = float(array[i])/45
        if (i == 1):
            array[i] = float(array[i])/30    
        if (i == 2):
            array[i] = float(array[i])/51
        array[i] = np.around(array[i], 5)
    return array
    
class Neural:
    def __init__(self):
        #deklaracja wag
        self.syn0 = 0
        self.syn1 = 0
        #czytanie zbioru treningowego
        file = "machinelearning_trainingset.csv"
        lines = open(file,"r").readlines()
        y = []
        x = []
        for line in lines:
            data = map(float, map(str.strip, line.split(";")))
            x.append(data[:3])
            tmpArr = []
            tmpArr.append(data[3])
            y.append(tmpArr)
            
        #normalizacja zb. treningowego
        for elem in x:
            for i in range (len(elem)):
                if (i == 0):
                    elem[i] = elem[i]/45
                if (i == 1):
                    elem[i] = elem[i]/30    
                if (i == 2):
                    elem[i] = elem[i]/51
                elem[i] = np.around(elem[i], 5)
        for elem in y:
            elem[0] = np.around(elem[0]/10, 5)
        x = np.array(x)
        y = np.array(y)
        
        #inicjalizacja wag losowymi wartosciami o sredniej zero
        np.random.seed(2)
        self.syn0 = 2*np.random.random((3,len(y))) - 1
        self.syn1 = 2*np.random.random((len(y),1)) - 1
        
        #petla uczaca
        for j in xrange(80000):

            #warstwa 0 = wejscie
            l0 = x
            #warstwa 1 - ukryta
            l1 = nonlin(np.dot(l0,self.syn0))
            #warstwa 2 - ostatnia
            l2 = nonlin(np.dot(l1,self.syn1))

            #blad
            l2_error = y - l2
            
            #blad razy pochodna -> wektor delta
            #jesli pochodna niewielka tzn oszacowanie bylo dosc pewne i nie powinnismy za bardzo zmieniac wag
            l2_delta = l2_error*nonlin(l2,deriv=True)

            #Propagacja wsteczna:
            #Bierzemy wektor delta (wazony blad) warstwy drugiej
            #i wysylamy go przez synapsy do warstwy pierwszej.
            #W ten sposob zachowujemy informacje o tym, jak bardzo
            #poszczegolne wezly w. 1. przyczynily sie do bledu w. 2.
            l1_error = l2_delta.dot(self.syn1.T)
            
            #blad razy pochodna -> wektor delta
            l1_delta = l1_error * nonlin(l1,deriv=True)
            
            #aktualizacja wag
            self.syn1 += l1.T.dot(l2_delta)
            self.syn0 += l0.T.dot(l1_delta)
    
    #funkcja przepuszczajaca prawdziwe dane przez nauczona siec
    def solve(self, array):
        array = normalize(array)
        l1 = nonlin(np.dot(array,self.syn0))
        result = nonlin(np.dot(l1,self.syn1))
        return result
        