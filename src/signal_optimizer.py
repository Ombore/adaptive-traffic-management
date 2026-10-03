class SignalOptimizer:

    def calculate_green_time(self, density):

        if density == "LOW":
            return 20

        if density == "MEDIUM":
            return 40

        if density == "HIGH":
            return 60

        return 30