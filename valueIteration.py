import random

# The value iteration algorithme to calulate the value function for each state


def valueIteration(states, actions, transitions, rewards, epsilon, gamma):
    # delta to mesure the difference between state values in precedent and current function
    delta = 1
    # initialise the value function to 0 for all states
    V = {s: 0.0 for s in states}
    i = 1
    # value iteration stop condition is a delta < epsilon
    while not delta < epsilon:
        # reinitialize delta for each iteration
        delta = 0
        # calculate V(s) = R(s,a) + sum T(s,a,s') V(s') : for all a in A
        for s in states:
            # keep a version of old value function to calculate delta
            v = V[s]
            # V(s) takes the max value over all values for all actions
            maxAction = float('-inf')
            for a in actions:
                Q = value(V, s, a, transitions, rewards, gamma)
                if Q > maxAction:
                    maxAction = Q
            V[s] = maxAction
            # caluclate delta = the maximum difference between old and new V for all states
            delta = max([delta, abs(V[s]-v)])
        # print the states values for the current iteration
        print("Values (it_" + str(i) + ") " +
              str(V) + " ; delta : " + str(delta))
        i += 1
    # return the optimal/converged (delta<epsilon) states values (value function)
    return V


# calculate V(s) = R(s,a) + sum T(s,a,s') V(s') : for a given a
def value(V, state, action, transitions, rewards, gamma):
    proba = transitions(state, action)
    va = rewards(state, action) + gamma * \
        sum([proba[next_state] * V[next_state] for next_state in proba])
    return va


# pi(s) = argmax V(s) for all a in A
# the policy for a given state returns the best action to perform in this state knowing V
def pi(V, state, actions, transitions, rewards, gamma):
    optimal_value = float('-inf')
    best_action = actions[0]
    for a in actions:
        v = value(V, state, a, transitions, rewards, gamma)
        if (v > optimal_value):
            optimal_value = v
            best_action = a
    return best_action


# get a random next state from possible next states with respect to transition probabilities
def rand(states_proba):
    r = random.random()
    index = 0
    states = [s for s in states_proba.keys()]
    s = states[index]
    while r > 0:
        s = states[index]
        if (r < states_proba[s]):
            return s
        else:
            r -= states_proba[s]
        index += 1
    return s


# Run an episode of game from a given initial state to end state following the optimal policy pi
def playEpisode(s0, isEnd, V, actions, transitions, rewards, gamma):
    state = s0  # set cursor to initial state
    print("---")
    print(V)
    print("---")

    while not isEnd(state):
        best_action = pi(V, state, actions, transitions, rewards, gamma)
        next_state = rand(transitions(state, best_action))
        reward = rewards(state, best_action)
        print("state = " + state + ", action = " + best_action +
              ", reward = " + str(reward) + ", next_state = " + next_state)
        state = next_state
