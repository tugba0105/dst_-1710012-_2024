final=[5]
input=input("write an input: ")
tape=[]
for x in range(0,len(input)):
    tape.append(input[x])
state=0
ponteiro=0
conf="("+str(state)+","+str(tape)+","+str(ponteiro)+")"
conf_c = "(" + str(state) + "," + str(tape[ponteiro]) + ")"
print("|-", conf)
computation_time=-1
while True:
    computation_time = computation_time+1

    match conf_c:
        case "(0,0)":
            state=1
            tape[ponteiro]="Z"
            ponteiro=ponteiro+1
        case "(1,0)":
            state = 1
            tape[ponteiro] = "X"
            ponteiro = ponteiro + 1
        case "(1,1)":
            state = 2
            tape[ponteiro] = "Y"
            ponteiro = ponteiro - 1
        case "(2,Y)":
            state = 2
            tape[ponteiro] = "Y"
            ponteiro = ponteiro - 1
        case "(2,X)":
            state = 3
            tape[ponteiro] = "Y"
            ponteiro = ponteiro + 1
        case "(2,Z)":
            state = 4
            tape[ponteiro] = "Z"
            ponteiro = ponteiro + 1
        case "(3,Y)":
            state = 3
            tape[ponteiro] = "Y"
            ponteiro = ponteiro + 1
        case "(3,1)":
            state = 2
            tape[ponteiro] = "Y"
            ponteiro = ponteiro - 1
        case "(4,Y)":
            state = 4
            tape[ponteiro] = "Y"
            ponteiro = ponteiro + 1
        case "(4,B)":
            state = 5
            tape[ponteiro] = "Z"
            ponteiro = ponteiro - 1
        case other:
            break;
    if ponteiro>=len(tape):
        tape.append("B")
    conf_c = "(" + str(state) + "," + str(tape[ponteiro]) + ")"
    conf = "(" + str(state) + "," + str(tape) + "," + str(ponteiro) + ")"
    print("|-",conf)

if state in final:
    print("the word",input," is recognized")
else:
    print("the word", input, " is not recognized")

print("input= ",input,",","size_input= ",len(input))
print("computation_space= ",len(tape))
print("computation_time= ",computation_time)
