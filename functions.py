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
	e = Task(i,c,a,b,d)
	task_queue.append(e)

task_queue.sort(key=operator.attrgetter('at','pr'))

# initializing all nodes

for i in range(n):
	f = Node(i,0,0,-1)
	node_list.append(f)

for i in task_queue:
	i.displaytask()

while(len(task_queue)!=0):

	templist = []

	for i in task_queue:
		
		# if the task hasn't arrived yet
		if(i.get_arrivaltime()>globaltime):
			break
		
		else:
			# remove task from incoming task list
			task_queue.remove(i)
			unassigned_node_count = 0
			
			# traverse through list of nodes to find available nodes
			for j in node_list:
				# if node status is waiting, it is available	
				if(j.get_nodestatus() == -1):
					print ("found free node")
					templist.append(j.get_nodeid())
					unassigned_node_count +=1
				# if req == availability, don't go further
				if(unassigned_node_count == i.get_req()):
					print ("found enough nodes")
					break

			# if enough nodes are not available, move task to waiting queue
			if(i.get_req()>unassigned_node_count):
				print ("Not enough nodes")
				waiting_queue.append(i)

			else:
				print ("added task")
				assigned_tasks.append(i)

				c = Cluster(random.randint(1,100),templist)
				cluster_list.append(c)

				for k in cluster_list:
					k.displaycluster()


			
	globaltime +=1
