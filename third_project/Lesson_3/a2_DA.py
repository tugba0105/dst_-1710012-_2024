final_states=[2,4]                                    # < ---------
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
                if(word[counter]=="0"):
                    state=1
                if (word[counter] == "1"):
                    state=2
                if (word[counter] != "0" and word[counter] != "1"): # quando nao occorem os anteriores
                    counter = counter - 1
                    break
            case 2:
                if (word[counter] == "0"):
                    state=3
                if (word[counter] == "1"):
                    counter = counter - 1
                    break
                if (word[counter] != "0" and word[counter] != "1"): # quando nao occorem os anteriores
                    counter = counter - 1
                    break
            case 3:
                if (word[counter] == "0"):
                    state=4
                if (word[counter] == "1"):
                    state = 3
                if (word[counter] != "0" and word[counter] != "1"): # quando nao occorem os anteriores
                    counter = counter - 1
                    break
            case 4:
                if (word[counter] == "0"):
                    counter=counter-1
                    break
                if (word[counter] == "1"):
                    state = 4
                if (word[counter] != "0" and word[counter] != "1"):  # quando nao occorem os anteriores
                    counter = counter - 1
                    break

    if(counter ==len(word)-1):
        counter=counter+1
        simulation = simulation + "|-(" + str(state) + "," + word[counter:] + ")\n"

    if(counter==len(word) and state in final_states):

        print("PT: palavra aceite,",word)
        print("EN: word accepted,", word)

    else:
        print("PT: palavra nao aceite,",word)
        print("EN: word not accepted,", word)
    print(simulation)
    word=""
    simulation=""
    print("********************")
    print("PT: introduza um valor (-1 para terminar): ")
    print("EN: introduce a value (-1 to end): ")
    word = input()

print("PT: automato terminado")
print("EN: automaton ended")

