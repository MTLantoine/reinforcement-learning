import random

# The value iteration algorithme to calulate the value function for each state


def qLearning(states, actions, transitions, rewards, epsilon, gamma):
    # delta to mesure the difference between state values in precedent and current function
    delta = 1
    # initialise the value function to 0 for all states
    Q = {s: 0.0 for s in states}
    i = 1
    # value iteration stop condition is a delta < epsilon
    while not delta < epsilon:
        # reinitialize delta for each iteration
        delta = 0
        # calculate V(s) = R(s,a) + sum T(s,a,s') V(s') : for all a in A
        for s in states:
            # keep a version of old value function to calculate delta
            v = Q[s]
            # V(s) takes the max value over all values for all actions
            maxAction = float('-inf')
            for a in actions:
                Q_prime = q(Q, s, a, transitions, rewards, epsilon, gamma)
                if Q_prime > maxAction:
                    maxAction = Q_prime
            Q[s] = maxAction
            # caluclate delta = the maximum difference between old and new V for all states
            delta = max([delta, abs(Q[s]-v)])
        # print the states values for the current iteration
        print("Values (it_" + str(i) + ") " +
              str(Q) + " ; delta : " + str(delta))
        i += 1
    # return the optimal/converged (delta<epsilon) states values (value function)
    return Q

# calculate V(s) = R(s,a) + sum T(s,a,s') V(s') : for a given a


def q(V, state, action, transitions, rewards, epsilon, gamma):
    proba = transitions(state, action)
    va = V[state] + epsilon * (rewards(state, action) + gamma *
                               max([V[next_state] for next_state in proba]) - V[state])
    # va = rewards(state, action) + gamma * \
    #     sum([proba[next_state] * V[next_state] for next_state in proba])
    return va


# pi(s) = argmax V(s) for all a in A
# the policy for a given state returns the best action to perform in this state knowing V
def pi(V, state, actions, transitions, rewards, epsilon, gamma):
    optimal_value = float('-inf')
    best_action = actions[0]
    for a in actions:
        v = q(V, state, a, transitions, rewards, epsilon, gamma)
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


def playEpisode(s0, isEnd, V, actions, transitions, rewards, epsilon, gamma):
    state = s0  # set cursor to initial state

    while not isEnd(state):
        best_action = pi(V, state, actions, transitions,
                         rewards, epsilon, gamma)
        next_state = rand(transitions(state, best_action))
        reward = rewards(state, best_action)
        print("state = " + state + ", action = " + best_action +
              ", reward = " + str(reward) + ", next_state = " + next_state)
        state = next_state
