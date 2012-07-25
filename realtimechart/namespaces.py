import gevent
from socketio.namespace import BaseNamespace

class MessageNamespace(BaseNamespace):
    """
    This socket namespace is responsible to manage
    business logic related to the socket service
    """
    def on_message(self,msg):

        def sendcpu():
            """
            Example realtime data. Calculate CPU utilization
            """
            prev = None
            while self.socket.connected:
                vals = map(int, [x for x in open('/proc/stat').readlines()
                                 if x.startswith('cpu ')][0].split()[1:5])
                if prev:
                    percent = (100.0 * (sum(vals[:3]) - sum(prev[:3])) /
                               (sum(vals) - sum(prev)))
                    self.emit("showdata",dict(point=percent))
                prev = vals
                gevent.sleep(0.5)
        self.spawn(sendcpu)
