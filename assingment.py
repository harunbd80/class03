#backend information
name=['Harun','Ovi','Roni','Rabbi','Asif','Joy']

while True:
    user_create=input('Enter any information you like : Read/Update/Delete/End)')
    #Ending
    if user_create =='End':
        print('Thank you very much for visiting our service')
        break
    
    #Raed
    elif user_create=='Read':
        print('Congratulation Sir! This is our name list :',name)
        
    #Update
    
    elif user_create =='Update':
        wrong_name=input('Enter Wrong Name :')
        right_name=input('Enter Update Name :')
        if wrong_name in name:
            nm=wrong_name.index(wrong_name)
            name[nm]=right_name
        else:
            print('Doesnt match your information')
        
        print('Your Update Name List :',name)
    #Delete
    elif user_create=='Delete':
        dl=input('Enter Delate Option :')
        if dl in name:
            name.remove(dl)
        else:
            print('Doesnt Match Delate option')
        
        print('Your list ',name)
    
    
    else:
        print('Doesnt Macth Information')

    