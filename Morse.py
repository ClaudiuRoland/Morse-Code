import winsound
import time

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second

dot=150
dash=400

morse = {'a':[dot,dash],'b':[dash,dot,dot,dot],'c':[dash,dot,dash,dot],'d':[dash,dot,dot],'e':[dot],'f':[dot,dot,dash,dot],'g':[dash,dash,dot],'h':[dot,dot,dot,dot],""
         'i':[dot,dot],'j':[dot,dash,dash,dash],'k':[dash,dot,dash],'l':[dot,dash,dot,dot],'m':[dash,dash],'n':[dash,dot],'o':[dash,dash,dash],'p':[dot,dash,dash],'q':[dash,dash,dot,dash],""
         'r':[dot,dash,dot],'s':[dot,dot,dot],'t':[dash],'u':[dot,dot,dash],'v':[dot,dot,dot,dash],'w':[dot,dash,dash],'x':[dash,dot,dot,dash],'y':[dash,dot,dash,dash],'z':[dash,dot,dot],""
         '0':[dash,dash,dash,dash,dash],'1':[dot,dash,dash,dash,dash],'2':[dot,dot,dash,dash,dash],'3':[dot,dot,dot,dash,dash],'4':[dot,dot,dot,dot,dash],'5':[dot,dot,dot,dot,dot],""
         '6':[dash,dot,dot,dot,dot],'7':[dash,dash,dot,dot,dot],'8':[dash,dash,dash,dot,dot],'9':[dash,dash,dash,dash,dot]}

def beep(msg):

    for i in msg:
        print(i)
        if i==' ':
            print('break')
            time.sleep(1)
        else:
            for j in morse[i.lower()]:            
                winsound.Beep(frequency, j)

        
msg = input('Enter a message: ')
beep(msg)
