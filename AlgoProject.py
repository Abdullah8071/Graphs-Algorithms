import networkx as nx
import matplotlib.pyplot as plt
import sys

import tkinter as tk
from tkinter import filedialog
import os

#Creating Window Object
win = tk.Tk()

#Adding Title
win.title('Algorithms Project')

win.geometry('500x300+500+300')

frame = tk.Frame(win, bg = 'darkslategray')
frame.place(relwidth = 15, relheight = 15)

#Defining Function

#------------------------Prims Algorithm-------------------------------#
        
def Create_Adjacency_Matrix(Node1, Node2, BandWidth, a):
    Adjacency_Matrix = [[0.0 for i in range(a)] for j in range(a)]

    for i in range(len(Node1)):
            Adjacency_Matrix[Node1[i]][Node2[i]] = BandWidth[i]

    return Adjacency_Matrix

def Find_Min_Vertex(Weights, Visited, a):
    Min_Vertex = -1

    for i in range(a):
        if Visited[i] == False and (Min_Vertex == -1 or Weights[i] < Weights[Min_Vertex]):
            Min_Vertex = i
    
    return Min_Vertex

def Apply_Prims(Ajacency_Matrix, a, Start_Index):
    Parent = []
    Weights = []
    Visited = []

    for i in range(a):
        Visited.append(False)
        Weights.append(sys.float_info.max)
    
    for i in range(a):
        Parent.append(0)

    Parent[Start_Index] = -1
    Weights[Start_Index] = 0.0

    for i in range(a):
        Min_Vertex = Find_Min_Vertex(Weights, Visited, a)
        Visited[Min_Vertex] = True

        for j in range(a):
            if Ajacency_Matrix[Min_Vertex][j] != 0 and Visited[j] == False:
                if Ajacency_Matrix[Min_Vertex][j] < Weights[j]:
                    Weights[j] =Ajacency_Matrix[Min_Vertex][j]
                    Parent[j] = Min_Vertex

    Child = []
    total = 0.0
    print("Prims Algorithm!!!")
    print("Source Node: " + str(Start_Index))
    for i in range(a):
        if Parent[i] == -1 and Weights[i] == 0.0:
            continue
        if Parent[i] < i:
            print("Node1: " + str(Parent[i]) + " Node2: " + str(i) + " BandWidth: " + str(Weights[i]))
            Child.append(i)
            total += Weights[i]
        else:
            print("Node1: " + str(i) + " Node2: " + str(Parent[i]) + " BandWidth: " + str(Weights[i]))
            Child.append(Parent[i])
            Parent[i] = i
            total += Weights[i]

    print("Prims Result: ",total)
    return Parent, Child, Weights

# for i in range(len(Node1)):
#     print("Node1: " + str(Node1[i]) + " Node2: " + str(Node2[i]) + " BandWidth: " + str(BandWidth[i]))


# for i in range(len(Adjacency_Matrix)):
#         print(Adjacency_Matrix[i])

#----------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------#
    
def Create_Initial_Matrix(Node1, Node2, BandWidth, a):
    Initial_Matrix = [[sys.float_info.max for i in range(a)] for j in range(a)]

    for i in range(a):
        Initial_Matrix[i][i] = 0.0

    for i in range(len(Node1)):
        Initial_Matrix[Node1[i]][Node2[i]] = BandWidth[i]

    return Initial_Matrix
#------------------------------------------------------------------------------------#

#----------------------Floyd-Warshall Algorithm----------------------------#
    
def Apply_Floyds_Algorithm(Initial_Matrix, a, Start_Index):
    for k in range(a):
        for i in range(a):
            for j in range(a):
                Initial_Matrix[i][j] = min(Initial_Matrix[i][j], Initial_Matrix[i][k] + Initial_Matrix[k][j])

    total = 0.0

    #print(Initial_Matrix[Start_Index])
    for i in range(a):
        total += Initial_Matrix[Start_Index][i]

    print("Floyd-Warshell Algorithm Result: ",total)

    print("Floyd-Warshall Algorithm!!!")
    for i in range(len(Initial_Matrix)):
       print(Initial_Matrix[i])
    return Initial_Matrix

# for i in range(len(Initial_Matrix)):
#         print(Initial_Matrix[i])

#---------------------------------------------------------------------------------------#

#-------------------------Bellman-Ford Algorithm------------------------------------#

def Apply_Bellman(Initial_Matrix, a, Start_Index):
    Previous = []
    Cost = []

    for i in range(a):
        Previous.append(0)
        Cost.append(sys.float_info.max)

    Previous[Start_Index] = -1
    Cost[Start_Index] = 0.0

    for k in range(a-1):
        for i in range(a):
            for j in range(a):
                if(Cost[i] + Initial_Matrix[i][j] < Cost[j]):
                    Cost[j] = Cost[i] + Initial_Matrix[i][j]
                    Previous[j] = i

    Next = []
    total = 0.0
    print("Bellman-Ford Algorithm!!!")
    #print("Source Vertex: " + str(Start_Index))
    for i in range(a):
        if i == Start_Index:
            continue
        print("Parent: " + str(Previous[i]) + " Node: " + str(i) + " Cost: " + str(Cost[i]))
        Next.append(i)
        total+=Cost[i]

    print("Bellmon Ford Result: ",total)
    return Previous, Next, Cost

#---------------------------------------------------------------------------------------#

#---------------------------Kruskal Algorithm------------------------------#

def ParentSearch(Source , Parent):
    if Parent[Source] == Source:
        return Parent[Source]
    else:
        return ParentSearch(Parent[Source],Parent)

def Kruskals(Node1,Node2,Bandwidth,a):
    KNode1=[]
    KNode2=[]
    KBandWidth=sorted(Bandwidth)
    for i in range(len(KBandWidth)):

        for j in range(len(Bandwidth)):
            if KBandWidth[i] == Bandwidth[j]:
                KNode1.append(Node1[j])
                
                KNode2.append(Node2[j])
                Bandwidth[j]=-11111  #Garbage Not To Repeat Value    
    sum1 = 0   
    Edge=[]
    FNode1=[]
    FNode2=[]
    
    Parent=[]
    
    for i in range(a):
        Parent.append(i)
    
    count=0
    j=0
    while count < a-1:
        Source = KNode1[j]
        Destination =KNode2[j]
        
        SParent=ParentSearch(Source , Parent)
        DParent=ParentSearch(Destination , Parent)
        if SParent != DParent:
            Edge.append(KBandWidth[j])
            FNode1.append(KNode1[j])
            FNode2.append(KNode2[j])
            count = count + 1
            Parent[SParent] = DParent    
        j = j + 1
       
   # for i in range(len(FNode1)):
    #    print(FNode1[i]," ", FNode2[i]," ",Edge[i])
   # print(len(FNode1)," " ,len(FNode2)," ",len(Edge))        
    for i in range(len(Edge)):
        sum1=sum1+Edge[i]
    print("Kruskals Result: ",sum1)

    G=nx.Graph()
    for i in range(a):
        G.add_node(i)
    for i in range(len(FNode1)):
        G.add_edge(FNode1[i],FNode2[i])
    # nx.draw_networkx(G,node_color ='green',node_size = 1000)

    return FNode1, FNode2, Edge

#-----------------------------------------------------------------------------------#

#--------------------------Dijikstra Algorithm------------------------------#

def FindMin(distance,visited,Num):
    MVertex=-1
    for i in range(Num):
        if visited[i] == False and (MVertex==-1 or distance[i] < distance[MVertex]):
            MVertex=i
    
    return MVertex        

def Dijkstra(Edges,Num,target):
    distance=[] 
    visited=[]
    
    index=[] #identifying whether already a edge is present or not
    parent=[0,0,0,0,0,0,0,0,0,0] #tracing it's parent
    initial=[]
    for i in range(Num):
        initial.append(i)
    
    for i in range(Num):
        index.append(False)
    for i in range (Num):
        distance.append(10000000000)
        visited.append(False)
    
    distance[target]=0.0
    index.insert(target,target)
    parent[target]=target
    # print(len(parent))
    #print(parent[2],index[2])
                        
    # G=nx.Graph()
    # for i in range(a):
    #     G.add_node(i,pos=(x_position[i],y_position[i]))
    
    for i in range(Num-1):
        MVertex=FindMin(distance,visited,Num)
        visited[MVertex]=True
        for j in range(Num):
            if Edges[MVertex][j] !=0 and visited[j] == False:
                dis= distance[MVertex]+Edges[MVertex][j]
                if dis<distance[j]:
                    distance[j] = dis
                    #index.insert(j,j)
                    if j!= target:
                        parent[j]=MVertex
                    # print(len(parent))
                    if index[j]==True:
                        print("")
                        # G.remove_node(j)
                        # G.add_node(j,pos=(x_position[j],y_position[j]))
                        # G.add_edge(MVertex,j,b=Edges[MVertex][j])
                    else:
                        # G.add_edge(MVertex,j,b=Edges[MVertex][j])
                        index[j]=True                    
    # print(len(parent),"\n")

    for i in range(len(parent)):
        print(parent[i]," ",i," ",distance[i])
    #fig,ax=plt.subplots()                  
    #pos=nx.get_node_attributes(G,'pos')
    #nx.draw_networkx(G,pos,node_color='Pink',edge_color='Purple',node_size=350,with_labels=True)
    #nx.draw_networkx_nodes(G,pos,ax=ax)
    #nx.draw_networkx_edge_labels(G,pos)
    
    #ax.tick_params(left=True,bottom=True,labelleft=True,labelbottom=True)
                    
    
    print("Dijikstra Algorithm!!!")
    summer=0                
    # for i in range(Num):
    #     print(target ," ",distance[i]," ",i," ")
    #     summer=summer+distance[i]
        
    print("Dijkstra Result: ",summer)

    return parent, initial, distance

#-----------------------------------------------------------------------------------#

def open_file():
    file_name = filedialog.askopenfilename(initialdir = "/desktop/benchmark", title = "Select a File", filetype = (("text files", ".*txt"), ("All Files", "*.*")))
    filename = os.path.basename(file_name)
    f = open(file_name, 'r')
    f.readline()
    f.readline()
    a=f.readline()
    a=int(a)
    f.readline()

    x_position=[]
    y_position=[]
    for i in range(a):
        b=f.readline()
        x,y,z=b.split("\t")
        x=int(x)
        y=float(y)
        z=float(z)
        x_position.append(y)
        y_position.append(z)

    Node1=[]
    Node2=[]
    BandWidth=[]
    j=0
    k=0
    num=0
    f.readline()
    for z in range(a):
        b=f.readline()
        x=b.split("\t")
        for i in range(len(x)-2):
            if i%2 == 0 and j==0:
                j=1
                Node1.append(num)
                temp=x[i+1]
                temp=int(temp)
                Node2.append(temp)
        
            elif i%2 == 0 and j==1:
                j=0
                temp=float(x[i+1])
                BandWidth.append(temp/10000000)
        num=num+1

    f.readline()
    target=f.readline()
    target=int(target)
    print("File has been Read!!!")

    l2 = tk.Label(frame, text = 'File Name:', bg = 'darkslategray', fg = 'thistle', height = 2, font = 'Verdana 13 italic')
    l2.grid(row = 2, column = 0, sticky = tk.W)

    l3 = tk.Label(frame, text = filename, bg = 'darkslategray', fg = 'thistle', height = 2, font = 'Verdana 13 italic')
    l3.grid(row = 2, column = 1)

    l4 = tk.Label(frame, text = 'Prims Algorithm', bg = 'darkslategray', fg = 'thistle', font = 'Verdana 13 italic')
    l4.grid(row = 3, column = 0, sticky = tk.W)

    l5 = tk.Label(frame, text = 'Kruskal Algorithm', bg = 'darkslategray', fg = 'thistle', font = 'Verdana 13 italic')
    l5.grid(row = 4, column = 0, sticky = tk.W)

    l6 = tk.Label(frame, text = 'Dijikstra Algorithm', bg = 'darkslategray', fg = 'thistle', font = 'Verdana 13 italic')
    l6.grid(row = 5, column = 0, sticky = tk.W)

    l7 = tk.Label(frame, text = 'Bellman Ford Algorithm', bg = 'darkslategray', fg = 'thistle', font = 'Verdana 13 italic')
    l7.grid(row = 6, column = 0, sticky = tk.W)

    l8 = tk.Label(frame, text = 'Floyd Warshall Algorithm', bg = 'darkslategray', fg = 'thistle', font = 'Verdana 13 italic')
    l8.grid(row = 7, column = 0, sticky = tk.W)

    # def Plot_Graph(x_position, y_position, a, target):


    def Prims():
        Ajacency_Matrix = Create_Adjacency_Matrix(Node1, Node2, BandWidth, a)
        Parent, Child, Weights = Apply_Prims(Ajacency_Matrix, a, target)

    def Kruskal():
        nd1 = Node1
        nd2 = Node2
        bd = BandWidth
        FNode1, FNode2, Edge = Kruskals(nd1,nd2,bd,a)
    
    def Dijikstra():
        Adjacency_Matrix = Create_Adjacency_Matrix(Node1, Node2, BandWidth, a)
        parent, initial, distance = Dijkstra(Adjacency_Matrix, a, target)
    
    def Bellman_Ford():
        Initial_Matrix = Create_Initial_Matrix(Node1, Node2, BandWidth, a)
        Previous, Next, Cost = Apply_Bellman(Initial_Matrix, a, target)
    
    def Floyd_Warshall():
        Initial_Matrix = Create_Initial_Matrix(Node1, Node2, BandWidth, a)
        Initial_Matrix = Apply_Floyds_Algorithm(Initial_Matrix, a, target)
    
    
    b1 = tk.Button(frame, text = 'Apply', bg = 'gray15', fg = 'thistle', font = 'Verdana 13 italic' ,command = Prims)
    b1.grid(row = 3, column = 1)

    b2 = tk.Button(frame, text = 'Apply', bg = 'gray15', fg = 'thistle', font = 'Verdana 13 italic' ,command = Kruskal)
    b2.grid(row = 4, column = 1)

    b3 = tk.Button(frame, text = 'Apply', bg = 'gray15', fg = 'thistle', font = 'Verdana 13 italic' ,command = Dijikstra)
    b3.grid(row = 5, column = 1)

    b4 = tk.Button(frame, text = 'Apply', bg = 'gray15', fg = 'thistle', font = 'Verdana 13 italic' ,command = Bellman_Ford)
    b4.grid(row = 6, column = 1)

    b5 = tk.Button(frame, text = 'Apply', bg = 'gray15', fg = 'thistle', font = 'Verdana 13 italic' ,command = Floyd_Warshall)
    b5.grid(row = 7, column = 1)


   
#Defining Labels
l1 = tk.Label(frame, text = 'Browse a File ', bg = 'darkslategray', fg = 'thistle', font = 'Verdana 13 italic')
l1.grid(row = 1, column = 0, sticky = tk.W)

#Defining Button
Browse_Button = tk.Button(frame, text = 'Browse', bg = 'gray15', fg = 'thistle', font = 'Verdana 13 italic' ,command = open_file)
Browse_Button.grid(row = 1, column = 1)

# array = [[0.0 for i in range(a)] for j in range(a)]
# for i in range(a):
#     for j in range(a):
#         array[i][j]=0        

# for i in range (len(Node1)):
#     array[Node1[i]][Node2[i]]=BandWidth[i]
    
# #Dijkstra Algorithm
# #------------------------------------------------------------------------------------#    

# def FindMin(distance,visited,Num):
#     MVertex=-1
#     for i in range(Num):
#         if visited[i] == False and (MVertex==-1 or distance[i] < distance[MVertex]):
#             MVertex=i
    
#     return MVertex        

# def Dijkstra (Edges,Num,target):
#     distance=[] 
#     visited=[]
    
#     index=[] #identifying whether already a edge is present or not
#     parent=[0,0,0,0,0,0,0,0,0,0] #tracing it's parent
    
#     for i in range(Num):
#         index.append(False)
#     for i in range (Num):
#         distance.append(10000000000)
#         visited.append(False)
    
#     distance[target]=0.0
#     index.insert(target,target)
#     parent.insert(target,target)
    
#     #print(parent[2],index[2])
                        
#     G=nx.Graph()
#     for i in range(a):
#         G.add_node(i,pos=(x_position[i],y_position[i]))
    
#     for i in range(Num-1):
#         MVertex=FindMin(distance,visited,Num)
#         visited[MVertex]=True
#         for j in range(Num):
#             if Edges[MVertex][j] !=0 and visited[j] == False:
#                 dis= distance[MVertex]+Edges[MVertex][j]
#                 if dis<distance[j]:
#                     distance[j] = dis
#                     #index.insert(j,j)
#                     parent.insert(j,MVertex)
#                     if index[j]==True:
#                         G.remove_node(j)
#                         G.add_node(j,pos=(x_position[j],y_position[j]))
#                         G.add_edge(MVertex,j,b=Edges[MVertex][j])
#                     else:
#                         G.add_edge(MVertex,j,b=Edges[MVertex][j])
#                         index[j]=True
#                     #print(j," ",parent[j]," ")
    
#     # fig,ax=plt.subplots()
#     # pos=nx.get_node_attributes(G,'pos')
#     # nx.draw_networkx(G, pos, node_color='Pink',edge_color='Purple',node_size=350,with_labels=True)
#     # nx.draw_networkx_nodes(G,pos,ax=ax)
#     # nx.draw_networkx_edge_labels(G,pos)
#     # plt.show()
#     fig,ax=plt.subplots()                  
#     pos=nx.get_node_attributes(G,'pos')
#     nx.draw_networkx(G,pos,node_color='Pink',edge_color='Purple',node_size=350,with_labels=True)
#     nx.draw_networkx_nodes(G,pos,ax=ax)
#     nx.draw_networkx_edge_labels(G,pos)
#     plt.show()

#     ax.tick_params(left=True,bottom=True,labelleft=True,labelbottom=True)
                    
#     summer=0                
#     for i in range(Num):
#         #print(target ," ",distance[i]," ",i," ")
#         summer=summer+distance[i]
        
#     print("Dijkstra Result: ",summer)

# #---------------------------------------------------------------------------------#
# #---------------------------------------------------------------------------------#    

# #--------------------------------------------------------------------------------#

# Dijkstra (array,a,target)

win.mainloop()