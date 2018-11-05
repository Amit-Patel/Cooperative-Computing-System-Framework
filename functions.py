from project_code import *
import operator
import random

n = input("Enter number of nodes for Resource Manager:")
t = input("Enter number of tasks:")
task_queue = []
assigned_tasks = []
cluster_list = []
waiting_queue = []
node_list = []
globaltime =0 

for i in range(t):
	a = input("Arrival time:")
	b = input("Duration:")
	c = input("Enter priority, 0 for HIGH 1 for LOW:")
	d = input("Number of resources required:")
	e = Task(i,c,a,b,d,[])
	task_queue.append(e)

task_queue.sort(key=operator.attrgetter('at','pr'))

# initializing all nodes

for i in range(n):
	f = Node(i,0,0,-1)
	node_list.append(f)

for i in task_queue:
	i.displaytask()

while(len(task_queue)!=0):

	
	#checking to assign new task
	for i in task_queue:
		
		# if the task hasn't arrived yet
		if(i.get_arrivaltime()>globaltime):
			break
		
		else:
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
				print ("added task")
				assigned_tasks.append(i)

				c = Cluster(random.randint(1,100),templist)
				cluster_list.append(c)
				
				#assigning task to nodes in cluster_list
				count = 0;
				for k in templist:
					node_list[k].set_clusterid(c.get_cluster())
					
					#first half runs the program
					if(count < len(templist/2)):
						node_list[k].set_currenttaskid(i.get_taskid())
						node_list[k].set_status(1)
						
					#second half is in standby
					else:
						node_list[k].set_status(0)
					
				
				for k in cluster_list:
					k.displaycluster()

	#removing clusters after execution
	for i in assigned_tasks:
		if(i.get_arrivaltime() + i.get_et() == globaltime):
		
			#reset attributes of nodes running the task
			for j in i.get_nlist():
				j.set_currenttaskid(0)
				j.set_status(-1)
				
			#if task in high priority
			if(i.get_taskpriority() == 0):
				cid = i.get_nlist()[0]
				
				#find the cluster running the task using cluster id
				for j in cluster_list:
					if(j.get_cluster() == cid):
						#remove the element from list
						cluster_list.remove(j)
						
						#set cid of each node in cluster to zero
						for k in j.get_cluster():
							k.set_clusterid(0)
						break;	
						
			#remove task from task_list
			assigned_tasks.remove(i)
	
	#try to execute task in waiting_queue
	#assumed that high priority tasks are not present
	for i in waiting_queue:
		count = 0
		templist = []
		
		#find free nodes to run task
		for j in node_list:
			if(j.get_nodestatus() == -1):
				count+=1
				templist.append(j.get_nodeid())
			if(count == i.get_req()):
				break;	
		
		if(count == i.get_req()):
			for j in templist:
				j.set_currenttaskid(i.get_taskid())
				j.set_status(0)
		
		
				
	globaltime +=1
