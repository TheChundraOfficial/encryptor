def decodibg():
    source = input("Введите число: ")
    print(f"Исходник: {source}")

    for i in source:
        if(i == '1' or i == '0'):
           pass 
        else:
            print("Ошибка: это не двоичное число")
            exit(0)

    final = 0
    for i in source:
        if(i == '1'):
            final = final * 2 + 1
        if(i == '0'):
            final = final * 2
        
    print(f"Расшифровка: {final}")    
  
    
def encryption():
    try:
        source = int(input("Введите число: "))
    except ValueError:
        print("Ошибка: вы ввели неккоректное число.")  
        exit(0)  
      
    final = ""  
      
    while source != 0:
        if(source % 2 == 1):
            source = int(source / 2)
            final = final + '1'
        else:    
            source = source / 2
            final = final + '0'
            
    final = final[::-1]        
            
    print(f"Зашифровка: {final}")        
    
    
def main():
    cmd = input("1 - расшифровка\n2 - зашифровка\nВведите номер действия: ") 
    
    if(cmd == "1"): 
        decodibg()
    elif(cmd == "2"):
        encryption()
    
    
if(__name__ == "__main__"):
    main()

