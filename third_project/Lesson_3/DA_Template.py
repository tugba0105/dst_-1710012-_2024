final_states=[1,3]  # final states
simulation=""
print("PT: introduza um valor (-1 para terminar) ")
print("EN: introduce a value (-1 to end): ")
word = input()
state=1 # initial state
while(word!="-1"):
    counter=-1 # counting
    state=1
    while(counter<len(word)-1):
        counter=counter+1
        if counter==0:
            simulation = simulation + "  (" + str(state) + "," + word[counter:] + ")\n"  # simulator
        else:
            simulation = simulation+"|-(" + str(state) + "," + word[counter:] + ")\n" # simulator
        match state:
            case 1:                                 
                if(word[counter]=="a"): # machine in state 1 reading 'a' go to the state 1
                    state=1
                if (word[counter] == "b"): # machine in state 'b' reading a go to the state 2
                    state=2
                if (word[counter] != "a" and word[counter] != "b"): # when a letter don't belong to the alphabet
                    counter = counter - 1
                    break
            case 2:
                if (word[counter] == "a"): # machine in state 2 reading 'a' is not possible
                    counter = counter - 1
                    break
                if (word[counter] == "b"): # machine in state 2 reading 'b' go to the state 3
                    state=3
                if (word[counter] != "a" and word[counter] != "b"): # when a letter don't belong to the alphabet
                    counter = counter - 1
                    break
            case 3:
                if (word[counter] == "a"): # machine in state 3 reading 'a' is not possible
                    counter = counter - 1
                    break
                if (word[counter] == "b"): # machine in state 3 reading 'b' go to the state 3
                    state = 3
                if (word[counter] != "a" and word[counter] != "b"): # when a letter don't belong to the alphabet
                    counter = counter - 1
                    break
    if (counter == len(word) - 1):
        counter = counter + 1
        simulation = simulation + "|-(" + str(state) + "," + word[counter:] + ")\n" # simulator

    if (counter == len(word) and state in final_states):
        print("PT: palavra aceite,", word)
        print("EN: word accepted,", word)

    else:
        print("PT: palavra nao aceite,", word)
        print("EN: word not accepted,", word)

    print(simulation) # print simualtion
    word = ""
    simulation = ""
    print("********************")
    print("PT: introduza um valor (-1 para terminar): ")
    print("EN: introduce a value (-1 to end): ")
    word = input()

print("PT: automato terminado")
print("EN: automaton ended")

