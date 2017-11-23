from datetime import datetime
import serial
import urllib2
import urllib

API_KEY="YOUR API KEY"

#CODIGO SERIAL
TEMPERATURA = "T"
LUMINOSIDADE = "L"
UMIDADE = "U"
SOLO = "S"
INDICE_CALOR = "I"
CHUVA = "C"

class Sensores:
  def __init__(self):
    self.temperatura=0
    self.luminosidade=0
    self.umidade=0
    self.solo=0
    self.i_calor=0
    self.chuva=0

  def enviar(self):
    url = "https://api.thingspeak.com/update"

    #DICIONARIO DE DADOS DOS SENSORES
    data={"api_key":API_KEY}
    data["field1"] = self.temperatura
    data["field2"] = self.umidade
    data["field3"] = self.i_calor
    data["field4"] = self.luminosidade
    full_url = "%s?%s" % (url,urllib.urlencode(data))

    try:
      print "Seq: %s" % (urllib2.urlopen(full_url).read(),)
    except urllib2.HTTPError:
      print "Falha no envio para Nuvem, continuando..."
    except:
      raise
      
def imprimir(self):                                      
    print "Temperatura: %sC" % (self.temperatura,)         
    print "Umidade: %s%%" % (self.umidade,)                
    print "Indice de Calor: %sC" % (self.i_calor,)         
    print "Solo: %s" % (self.solo,)                        
    print "Chuva: %s" % (self.chuva,)                      
    print "Luminosidade %s%%" % (self.luminosidade,)       
    print datetime.now()                                   
    print                                                  
                                                           
  def inserir(self,codigo,valor):                          
    if codigo == TEMPERATURA:                              
        self.temperatura=valor                             
    elif codigo == LUMINOSIDADE:                           
        self.luminosidade = valor                          
    elif codigo == UMIDADE:                                
        self.umidade=valor                                 
    elif codigo == SOLO:                                   
        self.solo=valor                                    
    elif codigo == INDICE_CALOR:                           
        self.i_calor = valor                               
    elif codigo == CHUVA:                                  
        self.chuva = valor                                 
    else:                                                  
      print "Codigo Inexistente, Continuando ..."    
      
def main():                                                                                                                                     
  texto=""                                                                                                                                      
  sensores = Sensores()                                                                                                                         
  with serial.Serial("/dev/ttyS1",9600) as arduino_serial:                                                                                      
    while True:                                                                                                                                 
      caracter = arduino_serial.read()                                                                                                          
      if caracter == "\n":                                                                                                                      
        sensores.enviar()                                                                                                                       
        sensores.imprimir()                                                                                                                     
        texto = ""                                                                                                                              
      elif "A" <= caracter <="Z":                                                                                                               
        sensores.inserir(caracter,texto)                                                                                                        
        texto = ""                                                                                                                              
      else:                                                                                                                                     
        texto += caracter                                                                                                                       
                                                                                                                                                
if (__name__=="__main__"):                                                                                                                      
  main()
      
