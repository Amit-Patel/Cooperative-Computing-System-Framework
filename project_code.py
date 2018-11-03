
class Node:

    def __init__(self,cid,ctid,stat):
        self.cid = cid
        self.ctid = ctid
        self.stat = stat

    def set_clusterid(self,value):
        self.cid = value

    def set_currenttaskid(self,value):
        self.ctid = value

    def set_status(self, value):
        self.stat = value

    def get_clusterid(self):
        return self.cid

    def get_currenttaskid(self):
        return self.ctid

    def get_nodestatus(self):
        return self.stat

class Task:

    def __init__(self,tid,pr,at,et,req):
        self.tid = tid
        self.pr = pr
        self.at = at
        self.et = et
        self.req = req

    def set_taskid(self, value):
        self.tid = value

    def set_taskpriority(self, value):
        self.pr = value

    def set_arrivaltime(self, value):
        self.at = value

    def set_et(self,value):
        self.et = value

    def set_req(self,value):
        self.req = value

    def get_taskid(self):
        return self.tid

    def get_taskpriority(self):
        return self.pr

    def get_arrivaltime(self):
        return self.at

    def get_et(self):
        return self.et
    
    def get_req(self):
        return self.req

t = Task(1,0,9,3,2)
print (t.get_et())

    

    

    
    
