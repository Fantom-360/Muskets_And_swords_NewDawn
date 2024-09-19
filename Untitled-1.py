while True:
    try:
        print("for 'YES' enter '1' and for 'NO' enter '0'\n")
        a = int(input("will we call today? "))
    except ValueError:
        print("something went wrong try something else")
        continue

    if a == 1:

        print("Satori is happy :D")

        u_in = int(input("when would it be ||in minutes||? "))

        break
        
    elif a == 0:

        print("Don't worry about Satori she will be fine ||maybe||, now mainly focus to have a great night.")
        break

   
        
