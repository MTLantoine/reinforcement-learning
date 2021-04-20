# GRID 6 probabilistic MDP model:

# set of states S
states= ["s"+str(i) for i in range(6) ]
# set of actions A
actions= ["right", "down", "left", "up" ]

# transition function T
def transitions(state, action):
    # Calculate next state (according to simple grid with wall)
    # 80% chance that the action excutes correctly, 20% chance stay still
    prob_reussite = 0.8
    next_states = {}
    
    # Default: remain in a state if action tries to leave grid
    next_states[state] = 1.0
    
    if (state == "s0" and action == "down") :
        next_states["s4"] = prob_reussite
        next_states[state] = 0.2
    elif (state == "s1" and action == "down") :
        next_states["s3"] = prob_reussite
        next_states[state] = 0.2
    elif (state == "s1" and action == "up") :
        next_states["s5"] = prob_reussite
        next_states[state] = 0.2
    elif (state == "s2" and action == "left") :
        next_states["s3"] = prob_reussite
        next_states[state] = 0.2
    elif (state == "s3" and action == "left") :
        next_states["s4"] = prob_reussite
        next_states[state] = 0.2
    elif (state == "s3" and action == "up") :
        next_states["s1"] = prob_reussite
        next_states[state] = 0.2
    elif (state == "s3" and action == "right") :
        next_states["s2"] = prob_reussite
        next_states[state] = 0.2
    elif (state == "s4" and action == "down") :
        next_states["s5"] = prob_reussite
        next_states[state] = 0.2
    elif (state == "s4" and action == "right") :
       next_states["s3"] = prob_reussite
       next_states[state] = 0.2
    elif (state == "s4" and action == "up") :
       next_states["s0"] = prob_reussite
       next_states[state] = 0.2

    return next_states

# reward function R
def rewards(state, action):
    # Calculate reward
    if (state == "s4" and action == "down") :
        return 10
    elif (state == "s1" and action == "up") :
        return 100
    elif (state == "s5") :
        return 0
    else:
        return -1


# final state
def isEnd(state):
    return (state == "s5")

