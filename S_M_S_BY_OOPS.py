import os
print('''                        
                        ######################################
                        ##### Student Management System  #####
                        ######################################
            ''')
class student():
    def __init__(self):
        pass
##----------------add new student-------------
    def add(self):
        f=open('.//students_project_data/student.txt','a+')
        f.seek(0,0)
##-------generate student id------
        no=0
        data_for_id=f.read()##---it will take all data in data_for_id variable-----
        if(data_for_id.startswith('[ No.: ')):
            f.seek(0,0)  ##-----for reading data from f in for loop cz pointer is at the end cz of f.read()-----
            for i in f: ##-----it will take data line by line in i----
              if(i.startswith('[ No.: ')):
                  l=i.split(' ')
                  no=int(l[2])
##-----end of generate id-----
        print('''
                               ##################################
                               # Enter Details For New Stident  #
                               ##################################
                                                                    ''')
        no+=1
        f_name=str(input("Enter Student First Name: "))
        s_name=str(input("Enter Student Second Name: "))
        age=str(input("Enter Age: "))
        branch=str(input("Enter Branch: "))
        gender=str(input("Enter Gender: "))
        f.write('[ No.: ' +str(no)+'   | First Name: '+f_name+'     | Last Name: '+s_name+'     | Gender: '+gender+'     | Age: '+str(age)+'     | Branch: '+branch+' ]\n')
        print('\nData has been added Succcessfully')
        f.close()
##--------------------view student----------
    def view(self):
        f=open('.//students_project_data/student.txt','a+')
        print('''
                               ##################################
                               #       View all Students        #
                               ##################################
                                                                    ''')
        f.seek(0,0)  ##--cz of a+ mode pointer is at the end by default in a+ mode------
        view_data=f.read()
        f.seek(0,0)  ##-----for reading data from f in for loop cz pointer is at the end cz of f.read()-----
        if(len(view_data)>0):
            for line in f:
                print('----------------------------------------------------------------------------------------------------------------------------------------------------')
                print(line)
                print('----------------------------------------------------------------------------------------------------------------------------------------------------')
        else:
            print('\nSorry, There is No data to show\n')
        f.close()
##---------------update student details by id------------
    def update(self):
        f=open('.//students_project_data/student.txt','a+')
        f.seek(0,0)
        print('''
                               ##################################
                               #     Update student details     #
                               ##################################
                                                                    ''')
##----showing data for update------
        view_data=f.read()
        f.seek(0,0)
        if(len(view_data)>0):
            for line in f:
                print('----------------------------------------------------------------------------------------------------------------------------------------------------')
                print(line)
                print('----------------------------------------------------------------------------------------------------------------------------------------------------')
        else:
            print('\nSorry, There is No data to Update\n')
            f.close()
##-------end of showing data for update-------
        id_for_delete=str(input('Enter student id for update: '))
        id_delete='[ No.: '+id_for_delete
        f.seek(0,0)  ##-----first time going in else block without this, why??-----
        read_data=f.read()
        f.seek(0,0)  ##--it is for FOR loop or for read f in for loop---
        if(read_data.count(str(id_delete))):
            f1=open('.//students_project_data/temp.txt','a+')
            for line in f:
                if(line.startswith(id_delete)):
                    f_name=str(input("Enter Student First Name: "))
                    s_name=str(input("Enter Student Second Name: "))
                    age=str(input("Enter Age: "))
                    branch=str(input("Enter Branch: "))
                    gender=str(input("Enter Gender: "))
                    f1.write('[ No.: ' +id_for_delete+'   | First Name: '+f_name+'     | Last Name: '+s_name+'     | Gender: '+gender+'     | Age: '+str(age)+'     | Branch: '+branch+'     | Gender: '+gender+' ]\n')
                else:
                    f1.write(line)
            f.close()
            os.remove('.//students_project_data/student.txt')
            f1.close()
            os.rename('.//students_project_data/temp.txt','.//students_project_data/student.txt')
            print('\nStudent Details has been Updated Succcessfully')
            f.close()
        else:
            print('Sorry, There is no data with This Id')
            f.close()
##-------------delete student details by id----------
    def remove(self):
        f=open('.//students_project_data/student.txt','a+')
        f.seek(0,0)
        print('''
                               ##################################
                               #        Delete Student          #
                               ##################################
                                                                    ''')
##----showing data ------
        view_data=f.read()
        f.seek(0,0)
        if(len(view_data)>0):
            for line in f:
                print('----------------------------------------------------------------------------------------------------------------------------------------------------')
                print(line)
                print('----------------------------------------------------------------------------------------------------------------------------------------------------')
        else:
            print('\nSorry, There is No data to show\n')
            f.close()
##-------end of showing -------
        id_for_delete=str(input('Enter student id for delete: '))
        id_for_delete='[ No.: '+id_for_delete
        f.seek(0,0)  ##-----first time going in else block without this, why??-----
        read_data=f.read()
        f.seek(0,0)  ##--it is for FOR loop or for read f in for loop---
        if(read_data.count(str(id_for_delete))):
            f1=open('.//students_project_data/temp.txt','a+')
            for line in f:
                if(line.startswith(id_for_delete)):
                    pass
                else:
                    f1.write(line)
            f.close()
            os.remove('.//students_project_data/student.txt')
            f1.close()
            os.rename('.//students_project_data/temp.txt','.//students_project_data/student.txt')
            print('\nStudent Details has been Deleted Succcessfully')
            f.close()
        else:
            print('Sorry, There is no data with This Id')
            f.close()
##--------------search student details by id--------------
    def search(self):
        f=open('.//students_project_data/student.txt','a+')
        f.seek(0,0)
        print('''
                               ##################################
                               #         Search Student         #
                               ##################################
                                                                    ''')
        id_for_search=str(input('Enter Student Id For Search: '))
        print()
        id_for_search='[ No.: '+id_for_search
        read_data=f.read()
        f.seek(0,0)  ##--it is for FOR loop or for read f in for loop---
        if(read_data.count(str(id_for_search))):
            for line in f:
                if(line.startswith(id_for_search)):
                    print(line)
        else:
            print('Sorry, There is no data with This Id')
        f.close()
##----------------------creating object ------------------------------
std=student()
while(1):
    print('''
                     ---------------------------------------------
                    |   Enter 1: To Add New Student               |
                    |   Enter 2: To View Student's Details        |
                    |   Enter 3: To Modify Student's Details      |
                    |   Enter 4: To Remove Student                |
                    |   Enter 5: To Search Student                |
                    |   Enter 6: To Exit                          |
                     --------------------------------------------- ''')
    user_input=int(input('\n\nPlease Enter Your Choice: '))
##------add new student-------------
    if(user_input==1):
        std.add()
##----view student----------
    if(user_input==2):
        std.view()
##-----update student details by id----
    if(user_input==3):
        std.update()
##-----delete student details by id----
    if(user_input==4):
        std.remove()
##-----search student details by id----
    if(user_input==5):
        std.search()
##-----exit with program----
    if(user_input==6):
        break
    return_input=str(input('\nWant to exit this program:y/n: '))
    if(return_input=='n'):
        continue
    else:
        break


