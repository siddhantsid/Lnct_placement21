import csv
import os
from time import sleep
#-----------------------------------------------------------------------
year=['2014','2015','2016','2017','2018','2019','2020']
def extract_csv(y):
    companies=[]
    filepath=f"/media/removable/sd/lnct/{y}.csv"  # just choose your path
    with open(filepath,'r') as cfile:
        data=csv.DictReader(cfile)
        for each in data:
            companies.append(each["CompanyName"])
        return companies
def count_companies(comp):
    counter={}
    finalcounter={}
    #global totalnumberofstudentsplaced
    for each in comp:
        counter[each]=counter.get(each,0)+1
    totalnumberofstudentsplaced=sum(counter.values())

    for k,v in counter.items():
        finalcounter[v]=k


    #print("Test2 passed")
    return sorted(finalcounter.items(),reverse=True),totalnumberofstudentsplaced
def echo_data(data,tnum):
  finaldata=list(data[0:9])  # top companies with highest placements
  others=0
  for each in data[10:]: # this will sum all the  numbers of left over companies
      others=others+each[0]

  for each in finaldata:
     percent=int((int(each[0])/tnum)*100)
     print(f"\033[1;34m{percent}%  \033[1;33m or {each[0]} out of {tnum} students placed in \033[1;34m {each[1]} ")


if __name__=="__main__":
   print("\033[1;31mThis small program will give you year wise data of placements in lnct \033[0m")
   while True:
    os.system("clear")
    print('''\033[1;32m choose which year placements you want to see:- \n
   [1]>>2014\n
   [2]>>2015\n
   [3]>>2016\n
   [4]>>2017\n
   [5]>>2018\n
   [6]>>2019\n
   [7]>>2020\n
   [8]>>Every Year\n
   [9]>>Exit
   \033[0m'''
   )
#---------------------------------------------------------------------------------------------------------------------
    c1=input("\033[1;43;m Enter Option No [1 to 8]#>>")

    if c1  ==  "1":
       os.system("clear")
       counter,totalnumberofstudentsplaced=count_companies(extract_csv(year[0]))
       print(f"\033[1;41mThis is the data of 2014\033[0m\n".center(80))
       echo_data(counter,totalnumberofstudentsplaced)
       sleep(25)
    elif c1  == "2":
      os.system("clear")
      counter,totalnumberofstudentsplaced=count_companies(extract_csv(year[1]))
      print(f"\033[1;41mThis is the data of 2015\033[0m\n".center(80))
      echo_data(counter,totalnumberofstudentsplaced)
      sleep(25)

    elif c1  ==  "3":
     os.system("clear")
     counter,totalnumberofstudentsplaced=count_companies(extract_csv(year[2]))
     print(f"\033[1;41mThis is the data of 2016\033[0m\n".center(80))
     echo_data(counter,totalnumberofstudentsplaced)
     sleep(25)

    elif c1  == "4":
     os.system("clear")
     counter,totalnumberofstudentsplaced=count_companies(extract_csv(year[3]))
     print(f"\033[1;41mThis is the data of 2017\033[0m\n".center(80))
     echo_data(counter,totalnumberofstudentsplaced)
     sleep(25)

    elif c1  == "5":
     os.system("clear")
     counter,totalnumberofstudentsplaced=count_companies(extract_csv(year[4]))
     print(f"\033[1;41mThis is the data of 2018\033[0m\n".center(80))
     echo_data(counter,totalnumberofstudentsplaced)
     sleep(25)
    elif c1 == "6":
     os.system("clear")
     counter,totalnumberofstudentsplaced=count_companies(extract_csv(year[5]))
     print(f"\033[1;41mThis is the data of 2019\033[0m\n".center(80))
     echo_data(counter,totalnumberofstudentsplaced)
     sleep(25)

    elif c1 =="7":
     os.system("clear")
     counter,totalnumberofstudentsplaced=count_companies(extract_csv(year[6]))
     print(f"\033[1;41mThis is the data of 2020\033[0m\n".center(80))
     echo_data(counter,totalnumberofstudentsplaced)
     sleep(25)

    elif c1 =="8":

        for each in range(len(year)):
            os.system("clear")
            print(f"\033[1;41mThis is the data of{year[each]}\033[0m".center(80))
            counter,totalnumberofstudentsplaced=count_companies(extract_csv(year[each]))
            echo_data(counter,totalnumberofstudentsplaced)
            sleep(3)
    elif c1 =="exit" or c1 == "e" or c1 =="9":
        print("\033[1;41m Exiting in 3 sec".center(80))
        sleep(3)
        break
    else:
        print("Wrong input".center(80))
        continue
        sleep(0.25)
exit()
