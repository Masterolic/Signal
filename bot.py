from signal import signal, SIGPIPE, SIG_DFL   
signal(SIGPIPE,SIG_DFL) 
for i in range(4000): 
    print(i)
