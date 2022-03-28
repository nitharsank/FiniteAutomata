def modThree(string):
    
    state=0 # set initial state to 0
    while(string):
            if string[0] not in ["0","1"]:   #if state and read value have a corresponding transition, take the transition
                return "string has a non-binary character "+str(string[0])+'.'
            if state==0 and string[0]=="1":
                    state=1
            elif state==1 and string[0]=="0":
                    state=2
            elif state==1 and string[0]=="1":
                    state=0
            elif state==2 and string[0]=="0":
                    state=1
            string=string[1:] #shorten string with each iteration
    return state

def finiteAutomata(states,alphabet,initialState,acceptingStates,transitions,string):
    
    if initialState not in states:
        return "initial state, "+str(initialState)+", not in states."
    
    for acceptingState in acceptingStates:
        if acceptingState not in states:
            return "accepting state, "+str(acceptingState)+", not in states."
        
    currentState=initialState #set initial state
    transitionRequirements=[] 
    resultTransitions=[]

    invalidTransitions=[]
    for transition in transitions: #the function takes in a list of lists with the following format [currentState, readValue, nextState] for each transition
        transitionRequirements.append([transition[0],transition[1]]) #split the transition list of lists for easier lookup
        resultTransitions.append(transition[2])
        state=transition[0]
        resultingstate=transition[2]
        if state not in states or resultingstate not in states:   #check if any transitions are invalid (require an invalid state or lead to an invalid state)
            invalidTransitions.append(transition)
            
    if (invalidTransitions):        
        return "invalid transitions: " + str(invalidTransitions)
    
    while(string):
        
        if string[0] not in alphabet:
            return "string contains invalid character " +str(string[0]) 
        
        if [currentState,string[0]] in transitionRequirements:
            currentState=resultTransitions[transitionRequirements.index([currentState,string[0]])] #if state and read value have a corresponding transition, take the transition
        string=string[1:]
        
    return currentState if currentState in acceptingStates else "not accepting state."


