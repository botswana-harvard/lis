# http://stackoverflow.com/questions/1191374/subprocess-with-timeout (jcollado)
import subprocess
import threading


class Command(object):

    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout=5):
        def target():
            print 'Thread started'
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.communicate()
            print 'Thread finished'

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print 'Terminating process'
            self.process.terminate()
            thread.join()
        print self.process.returncode
