from project_code import *
import operator
import random
import numpy
from numpy import *

lines = loadtxt("sample.txt", comments="#", delimiter=",", unpack=False)
lines = lines.astype(numpy.int64)
print (len(lines))
print (lines)

#n = int(input("Enter number of nodes for Resource Manager:"))
#t = int(input("Enter number of tasks:"))
n = lines[0]
t = lines[1]

task_queue = []
assigned_tasks = []
cluster_list = []
waiting_queue = []
node_list = []
globaltime =0 

for i in range(t):

	a = lines[2+i*4]
	b = lines[2+i*4+1]
	c = lines[2+i*4+2]
	d = lines[2+i*4+3]
	e = Task(i,c,a,b,d,[])
	task_queue.append(e)

task_queue.sort(key=operator.attrgetter('at','pr'))

# initializing all nodes

for i in range(n):
	f = Node(i,0,-1,-1)
	node_list.append(f)

for i in task_queue:
	i.displaytask()

while(len(task_queue)!=0 or len(assigned_tasks)!=0):
	#if(globaltime==4):
	#	break
	#checking to assign new task
	for i in task_queue:
		
		# if the task hasn't arrived yet
		if(i.get_arrivaltime()>globaltime):
			break
		
		#for high priority task
		elif(i.get_taskpriority() == 0):
			# remove task from incoming task list
			task_queue.remove(i)
			unassigned_node_count = 0
			templist = []
			# traverse through list of nodes to find available nodes
			for j in node_list:
				# if node status is waiting, it is available	
				if(j.get_nodestatus() == -1):
					print ("found free node")
					templist.append(j.get_nodeid())
					unassigned_node_count +=1
				# if req == availability, don't go further
				if(unassigned_node_count == 2*i.get_req()):
					print ("found enough nodes")
					break

			# if enough nodes are not available, move task to waiting queue
			#high priority tasks double required nodes for backup
			if((2*i.get_req())>unassigned_node_count):
				print ("Not enough nodes")
				waiting_queue.append(i)

			else:
				activelist = []
				print ("added task")
				assigned_tasks.append(i)
				#i.set_nodelist(templist)
				c = Cluster(random.randint(1,100),templist)
				cluster_list.append(c)
				
				#assigning task to nodes in cluster_list
				count = 0;
				for k in templist:
					node_list[k].set_clusterid(c.get_clusterid())
					
					#first half runs the program
					if(count < len(templist)/2):
						node_list[k].set_currenttaskid(i.get_taskid())
						node_list[k].set_status(1)
						activelist.append(k);
					#second half is in standby
					#else:
					#	node_list[k].set_status(0)
					i.set_nodelist(activelist)
					count +=1
		#for low priority task push it into waiting_queue
		else:
			task_queue.remove(i)
			waiting_queue.append(i)
			
	rem = []						
	#removing clusters after execution
	for i in assigned_tasks:
		if(i.get_arrivaltime() + i.get_et() == globaltime):
			print("AT TIME T=",globaltime)
			#reset attributes of nodes running the task
			for j in i.get_nlist():
				node_list[j].set_currenttaskid(-1)
				node_list[j].set_status(-1)
			
			#if task in high priority
			if(i.get_taskpriority() == 0):
				print(i.get_nlist())
				nid = node_list[i.get_nlist()[0]]
				
				#find the cluster running the task using cluster id
				for j in cluster_list:
				
					if(j.get_clusterid() == nid.get_clusterid()):
						#remove the element from list
						cluster_list.remove(j)
						
						#set cid of each node in cluster to zero
						for k in j.get_cluster():
							node_list[k].set_clusterid(0)
						break	
						
			#rem contains the list of tasks to remove from task_list
			rem.append(i)
			
	for k in rem:
		assigned_tasks.remove(k)
	

	#try to execute task in waiting_queue
	#assumed that high priority tasks are not present
	for i in waiting_queue:
		count = 0
		#contains list of nodes selected for the task
		templist = []
		
		#low priority
		if(i.get_taskpriority() == 1):
			print("LOW PT TASK FROM WAAIT QUUEE")
			for j in node_list:
				
				if(j.get_nodestatus() == -1):
					count+=1
					templist.append(j.get_nodeid())
			print("NODES AVAILABLE", templist)
			
			if(count >= i.get_req()):
				
				for k in templist[:i.get_req()]:
					node_list[k].set_currenttaskid(i.get_taskid())
					node_list[k].set_status(0)
				
				i.set_nodelist(templist[:i.get_req()])
				i.set_arrivaltime(globaltime)
				assigned_tasks.append(i)
				waiting_queue.remove(i)
				
		#high priority
		else:
			print("HP TASK FROM WAITING QUEUE")
			for j in node_list:
				if(j.get_nodestatus() == -1 and j.get_clusterid() == 0):
					count+=1
					templist.append(j.get_nodeid())
			print(count,templist)
			if(count >= 2*i.get_req()):
				print("ENOUGH TIMES")
				#contains set of nodes running the task
				activelist = []
				for k in templist[:i.get_req()]:
					node_list[k].set_currenttaskid(i.get_taskid())
					node_list[k].set_status(1)
						
					activelist.append(k);
					
				c = Cluster(random.randint(1,100),templist[:(i.get_req()*2)])
				cluster_list.append(c)
				
				for k in templist[:2*i.get_req()]:
					node_list[k].set_clusterid(c.get_clusterid())
				
				i.set_nodelist(activelist)
				i.set_arrivaltime(globaltime)
				assigned_tasks.append(i)
				waiting_queue.remove(i)
				print("REMOVING TASK FROM WAITING QUEUE", waiting_queue)
		
		#find free nodes to run task
		#for j in node_list:

			
			# if(j.get_nodestatus() == -1):
				
				#for low priority
				# if(i.get_taskpriority() == 1):
					# count+=1
					# templist.append(j.get_nodeid())

				# high priority
				# priority is high and node is not part of  cluster
				# elif(j.get_clusterid() == 0):
					# count+=1
					# templist.append(j.get_nodeid())

				
				
			#for low priority task
			# if(count == i.get_req()):
				# for k in templist:
					# node_list[k].set_currenttaskid(i.get_taskid())
					# node_list[k].set_status(0)

				# i.set_nodelist(templist)
				# assigned_tasks.append(i)
				# waiting_queue.remove(i)
				# break
		
		
			# elif(count == 2*i.get_req()):
		
			
   
	print ("TIME  = ",globaltime)

	print("NODES----------")
	for k in node_list:
		k.displaynode()

	print("TASKS----------")
	for k in assigned_tasks:
		k.displaytask()

	print("CLUSTERS----------")
	for k in cluster_list:
		k.displaycluster()

	print("------------------------------------------")
	globaltime +=1
