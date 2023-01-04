from agent import Agent
import random


def dorianyou_policy(agent: Agent) -> str:
    """
    Policy of the agent
    return "left", "right", or "none"
    """


    """
    Get Rewards Know Emplacement and Agent Actual Position
    """
    rewards = agent.known_rewards
    pos = agent.position


    """
    Set Possible Actions
    """
    actions = ["none"]
    if (pos > 0):
        actions.append("left")
    if (pos < 7):
        actions.append("right")
    
    
    """
    Choose an Action
    """
    action = random.choice(actions)

    if (pos > 0 and rewards[pos] < rewards[pos-1]):
        action = "left"
        if (pos < 7 and rewards[pos] < rewards[pos+1]):
            action = "right"
    if (pos < 7 and rewards[pos-1] < rewards[pos+1]):
        action = "right"

    ##assert action in actions
    return action
