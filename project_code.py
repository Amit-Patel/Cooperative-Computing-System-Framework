class Cluster:

    #   cid - cluster id
    #   nlist - list of nodes part of the cluster, the active node will be the first element
    
    def __init__(self,cid,nlist):
        self.cid = cid
        self.nlist = nlist

    def set_clusterid(self,value):
        self.clusterid = value

    def initialize_cluster(self, nodelist):
        self.nlist = nodelist

    def get_clusterid(self):
        return self.cid

    def get_cluster(self):
        return self.nlist

    def displaynodelist(self):
    	for i in self.nlist:
    	    print ("Node:\t",i)

    def displaycluster(self):
    	print ("Cluster id:\t", self.get_clusterid())
    	print ("List of nodes:")
    	self.displaynodelist()

    	
    
class Node:

    # nid - node id
    # cid - cluster to which it belongs
    # ctid - current task executing on the node
    # stat - status of the node, ACTIVE(1), STANDBY(0), WAITING(-1)
											#0 should be for nodes running low priority
    def __init__(self,nid,cid,ctid,stat):
        self.nid = nid
        self.cid = cid
        self.ctid = ctid
        self.stat = stat

    def set_nodeid(self,value):
        self.nid = value

    def set_clusterid(self,value):
        self.cid = value

    def set_currenttaskid(self,value):
        self.ctid = value

    def set_status(self, value):
        self.stat = value

    def get_nodeid(self):
        return self.nid
    
    def get_clusterid(self):
        return self.cid

    def get_currenttaskid(self):
        return self.ctid

    def get_nodestatus(self):
        return self.stat

    def displaynode(self):
    	print ("Node id:\t", self.get_nodeid())
    	print ("Cluster id:\t", self.get_clusterid())
    	print ("Current task id:\t", self.get_currenttaskid())
    	print ("Status:\t", self.get_nodestatus())

class Task:

    #   tid - task id
    #   pr - priority of task
    #   at - arrival time
    #   et - estimated execution time
    #   req - resource requirements (number of nodes)
	#	nlist - list of nodes running the task
    
    def __init__(self,tid,pr,at,et,req,nlist):
        self.tid = tid
        self.pr = pr
        self.at = at
        self.et = et
        self.req = req
        self.nlist = nlist
		
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

    def set_nodelist(self,nlist):
        self.nlist = nlist
	
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
		
    def get_nlist(self):
        return self.nlist

    def displaytask(self):
        print ("Task id:\t", self.get_taskid())
        print ("Arrival Time:\t", self.get_arrivaltime())
        print ("Execution Time:\t", self.get_et())
        print ("Priority:\t", self.get_taskpriority())
        print ("Resources:\t", self.get_req())
        print ("Node list:\t", self.nlist, "\n")



#t = Task(1,0,9,3,2)
#print (t.get_et())

