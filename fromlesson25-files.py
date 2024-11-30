#workers_file=open("textfile","r")
#print(workers_file.readable()) # return boolean
#print(workers_file.read()) 
#print(workers_file.readline()) #read first line and put cursor on the second line to start read from it and so on
#print(workers_file.readlines()) #read all lines and put it in list
#print(workers_file.readlines()[0]) #read specfic line 
#workers_file.close()



######################  writing  ####################


workers_file=open("textfile","a")
#workers_file.write("\nthis is by appen mode two")
list_of_phases=["\nfirst phase","\nsecond phase","\nthird phase"]
workers_file.writelines(list_of_phases)  #to write multiple line
workers_file.close()


#################### test write file name not excist ###############
# workers_file=open("textfile2","a")
# workers_file.write("\nthis is by appen mode two")
# workers_file.close()