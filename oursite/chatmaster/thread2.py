import threading,time
class t(threading.Thread):
    def __init__(self,daemon):
        threading.Thread.__init__(self)
        self.daemon=daemon
    def run(self):
        x=0
        while 1:
            if self.daemon :
                print "Daemon :: %s" % x
            else :
                print "Non - Daemon :: %s" % x
            x+=1
            time.sleep(1)

q=t(True)
q.start()
print 'hello'
time.sleep(5)
print 'hello'
