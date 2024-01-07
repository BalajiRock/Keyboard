import threading
from pygame import mixer
import time

f = open("note.txt",'r')   
file_path = "piano-keys\\Piano.ff."

global content
global length
global remainder
content = f.readlines()
length = int(len(content)/8)
remainder = len(content)%8

def play_audio(file_path,duration,start_time,channel_no):
    print(time.time())
    time.sleep(start_time)
    mixer.init() 
    mixer.Channel(channel_no).play(mixer.Sound(file_path))
    time.sleep(duration)
    mixer.Channel(channel_no).stop()
      
def callback(thread_no):
    no_of_loops = length
    if(remainder>thread_no):
        no_of_loops+=1
    for i in range(no_of_loops):
        start_time,note,duration = content[i*8+thread_no].split()
        play_audio(file_path+note+".aiff",float(duration),float(start_time),thread_no) 
    return

x1 = threading.Thread(target=callback,args=(0,))
x2 = threading.Thread(target=callback,args=(1,))
x3 = threading.Thread(target=callback,args=(2,))
x4 = threading.Thread(target=callback,args=(3,))
x5 = threading.Thread(target=callback,args=(4,))
x6 = threading.Thread(target=callback,args=(5,))
x7 = threading.Thread(target=callback,args=(6,))
x8 = threading.Thread(target=callback,args=(7,))

x1.start()
x2.start()
x3.start()
x4.start()
x5.start()
x6.start()
x7.start()
x8.start()
    
x1.join()
x2.join()
x3.join()
x4.join()
x5.join()
x6.join()
x7.join()
x8.join()
f.close()