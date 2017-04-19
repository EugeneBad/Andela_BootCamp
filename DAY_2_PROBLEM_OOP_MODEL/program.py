class Disease:
    def __init__(self, prevalence, survival_rate):
        self.prevalence = prevalence  # Percentage of people who have the disease
        self.survival_rate = survival_rate  # How many people can survive the disease

    # Method that returns the number of infected people given an area's population
    def infected(self, population):
        return (population * self.prevalence)/100

    # Method that returns the number of people who will survive given an area's population
    def survive(self, population):
        num_infected = self.infected(population)
        return num_infected * self.survival_rate/100

    # Method that returns the number of people who will die given an area's population
    def death(self, population):
        num_infected = self.infected(population)
        return num_infected * (100 - self.survival_rate)/100


class Cancer(Disease):
    def __init__(self, terminal):
        self.prevalence = 45
        self.survival_rate = 70
        self.terminal = terminal  # True to mean cancer is terminal, False means otherwise.

    # Method that returns the survivors given an area's population
    def survive(self, population):
        if self.terminal:
            return 0

        else:
            num_infected = (population * self.prevalence)/100
            return num_infected * self.survival_rate/100

    # Method that returns the people who will die given an area's population
    def death(self, population):
        if self.terminal:
            return self.infected(population)

        else:
            num_infected = (population * self.prevalence)/100
            return num_infected * (100 - self.survival_rate)/100
