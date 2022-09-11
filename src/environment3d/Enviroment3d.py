

class Environment3d:


    def __init__(self):
        self.temporal = 0
        self.etiqueta = 0
        self.traduccion = ''


    


    # inicio concatenacion de 3d
    def cabecera(self):
        self.traduccion += '''
        /*------------- HEADER --------------*/ 
        # include <stdio.h>
        # include <math.h>

        float heap[10000];
        float stack[10000];
        float P;
        float H;

        
        float t0, t1, t2, t3, t4 ;




        /*------------- NATIVAS --------------*/
        
        void printString(){
            /*------(tamanio del arreglo)------*/
            t1 = t0;

            /*------(inicio del arreglo)------*/
            t3 = heap[(int)t2];

            /*------(contador del for)------*/
            t4 = 0;
            IMPRIMIR:
                if(t4 == t1) goto FINIMPRIMIR;
                printf("%c",(char)t3);
            
                t2 = t2 + 1;
                t3 = heap[(int)t2];
                t4 = t4 + 1;
                goto IMPRIMIR;
                FINIMPRIMIR:
                return;
        }       




        /*------------- INICIO -----------------*/

        void main(){
            P = 0;
            H = 0;
            return;
        }

        ''' 



    # metodo para obtener la cadena de la traduccion
    def getCadena(self):
        return self.traduccion




    # metodo pra concatenar la traduccion
    def concatenarTraduccion(self, cadena):
        self.traduccion += self.traduccion + cadena



    # metodo para aumentar el numero del temporal
    def aumentarTemporal(self):
        self.temporal += 1


    # obtener el numero del temporal actual
    def obtenerTemporal(self):
        return self.temporal




    # metodo para aumetar el numero de las etiquetas
    def aumentarEtiqueta(self):
        self.etiqueta += 1



    # etiqueta para aumetar la etiqueta
    def obtenerEtiqueta(self):
        return self.etiqueta

