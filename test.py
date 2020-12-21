from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):

    def __str__(self):
        return "<Agent: {}>".format(self._name)


class Ticket(object):
    pass


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:

        raise NotImplemented


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented

ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills = ["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

least_loaded_policy = LeastLoadedAgent()
# returns the Agent with name "B" because of their currently lower load.
least_loaded_policy.find(ticket, [agent1, agent2])

least_flexible_policy = LeastFlexibleAgent()
# returns the Agent with name "A" because of their lower flexibility.

least_flexible_policy.find(ticket, [agent1, agent2])