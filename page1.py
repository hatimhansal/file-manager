import os

import time

def NameUser():
    test=os.getcwd()
    path_tablaeu =test.split('/')
    for i in range(len(path_tablaeu)):
        if path_tablaeu[i] == 'home' or path_tablaeu[i] == "Home" :           
            user_exists=1
            get_userName=path_tablaeu[i+1] 
            return get_userName
            
    return "anonymous"

def Menu (): 

    print(f"""
    ===== File Manager =====  ({NameUser()})
    0. Menu 
    1. Show current directory
    2. List files
    3. Create directory
    4. Delete file
    5. Check path
    6. Exit
    7.Cherche file

    """)

Menu()

def cherche_file(name):
    path = os.getcwd()
    result_list=[]
    for root, dirs, files in os.walk(path):
        for file in files :
            if name in file :
                result_list.append(os.path.join(root,file))
        return result_list
                
            
    return None

def Aficher():
    print(os.getcwd())

def Affiche_inside(path):
    print(f" Path Before : {os.getcwd()}")
    if os.path.isdir(path) :
        nombr= os.listdir(path)
        print("*  List files : ")
        for i in range(len(nombr)) :
            full_path =os.path.join(path,nombr[i])
            
            if os.path.isdir(full_path):
                print(i,")","📁",nombr[i])
            elif os.path.isfile(full_path) :
                size = os.path.getsize(full_path)
                print(i,")","📄",nombr[i],"-",size,"bytes")
            else :
                print(i,")",nombr[i])
    else :
        print(" directory not found ")

def Create_dirct(path):
    if not path :
        print(" you entre path empty")
    elif os.path.exists(path) :
        print("* is alerdy exists ")
        if os.path.isdir(path):
            print("* found is directroy ")
        elif os.path.isfile(path):
            print("* found is file ")
        
    else :
        os.makedirs(path)
        print("Directory created ")
   
    
def Remove_file(path):
    try :
        while True :
            if os.path.isfile(path) :
                print(f"found  📄{path}")
                valid=input( " are you want Remove this file (y/n) :")
                time.sleep(1)
                if  valid.lower() == "y" :
                    os.remove(path)

                    print(" * Remove success")
                    break
                elif valid.lower() == "n" :
                    print("* File  not Remove")
                    break
            elif os.path.isdir(path) :
                print(f"found is 📁  not file {path} ")
            
                time.sleep(1)
                
                value_path=os.listdir(path)
                if value_path :
                    print(" is not empty")
                    print( " can't remove  folder")
                    break
                else :
                    Rmv_dirct=input(f"are you want Remove this folder {path} (y/n) :")
                    if Rmv_dirct.lower() == "y" :
                        os.rmdir(path)
                        break
                    elif Rmv_dirct.lower() == "n" :
                        print("Folder not Remove ")
                        break
            else :
                print(" File not found ")
    except OSError:
        print("file not found")

def Check_dirct_exist(path):
    if os.path.isdir(path) :
        print(" * ","📁",path,"is exist ")
    elif os.path.isfile(path):
        print(" * ","📄",path,"is exist")   
    else :
        print( f"* {path} Not  found ")

while True :
  
    choix = input(" Choses (1 To 7) or (0 Menu )  :")
    if choix == "1":
        Aficher()
    elif choix == "2":
        path = input( " Entre the path  or (e) :")
        if path == ""  or path =="e":
           tack_path=os.getcwd()
        else :
            tack_path = path
        Affiche_inside(tack_path)
        
    elif choix == "3" :
        path=input( "Entre path directory :")
        Create_dirct(path)

    elif choix == "4" :
        path = input( "Entre path file :")
        Remove_file(path)
    elif choix == "5":
        path = input( " Entre the path  :")
        Check_dirct_exist(path)
    elif choix == "6":
        print(" close")
        break
    elif choix == "7":
        name = input(" Entre the file name :")
        result = cherche_file(name)
        if result :
            print(f"* File is exists {result}")
        else : 
            print(f" * File not found {name} ")
    elif choix == "0":
        Menu()

    else :
        print(" Need Choses 1 - 7  or (0 Menu ) ")
        time.sleep(1)
        