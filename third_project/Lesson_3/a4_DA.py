final_states=[3]                                    # < ---------
simulation=""
print("PT: introduza um valor (-1 para terminar) ")
print("EN: introduce a value (-1 to end): ")
word = input()
state=1 # estado inicial
while(word!="-1"):
    counter=-1 # contador
    state=1
    while(counter<len(word)-1):
        counter=counter+1
        if counter == 0:
            simulation = simulation + "  (" + str(state) + "," + word[counter:] + ")\n"  # simulator
        else:
            simulation = simulation + "|-(" + str(state) + "," + word[counter:] + ")\n"  # simulator
        match state:
            case 1:                                 
                if(word[counter]=="a"):
                    state=1
                if (word[counter] == "b"):
                    state=2
                if (word[counter] == "c"):
                    counter = counter - 1
                    break
                if (word[counter] != "a" and word[counter] != "b" and word[counter] != "c"): # quando nao occorem os anteriores
                    counter = counter - 1
                    break
            case 2:
                if (word[counter] == "a"):
                    counter = counter - 1
                    break
                if (word[counter] == "b"):
                    counter = counter - 1
                    break
                if (word[counter] == "c"):
                    state=3
                if (word[counter] != "a" and word[counter] != "b" and word[counter] != "c"): # quando nao occorem os anteriores
                    counter = counter - 1
                    break
            case 3:
                if (word[counter] == "a"):
                    state=3
                if (word[counter] == "b"):
                    counter = counter - 1
                    break
                if (word[counter] != "a" and word[counter] != "b" and word[counter] != "c"): # quando nao occorem os anteriores
                    counter = counter - 1
                    break
    if (counter == len(word) - 1):
        counter = counter + 1
        simulation = simulation + "|-(" + str(state) + "," + word[counter:] + ")\n"

    if (counter == len(word) and state in final_states):
        print("PT: palavra aceite,", word)
        print("EN: word accepted,", word)

    else:
        print("PT: palavra nao aceite,", word)
        print("EN: word not accepted,", word)

    print(simulation)
    word = ""
    simulation = ""
    print("********************")
    print("PT: introduza um valor (-1 para terminar): ")
    print("EN: introduce a value (-1 to end): ")
    word = input()

print("PT: automato terminado")
print("EN: automaton ended")

    # state=1  #initial state
    # if(word=="-1" and state in final_states):
    #    print("palavra vazia aceite")
    # else:
    #    print("palavra vazia não aceite")
