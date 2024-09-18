while True:
    try:
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

    else:
        print("you can input only 1/0")
        continue
