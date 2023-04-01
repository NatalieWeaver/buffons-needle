import random
import math
import statistics

class Needle:
    def __init__(self, r):
        self.r = r
        self.angle = random.random() * 2 * math.pi
        self.x1 = random.random() * 10
        self.y1 = random.random() * 10
        self.x2 = self.x1 + self.r * math.cos(self.angle)
        self.y2 = self.y1 + self.r * math.sin(self.angle)
        self.outcome = self.calculate_outcome()

    def calculate_outcome(self):
        outcome = abs(math.floor(self.x2) - math.floor(self.x1))
        assert outcome in [0, 1]
        return outcome
    

class Experiment:
    def __init__(self, r=1):
        self.r = r
        self.needles = []
        self.pi_est = 1

    def drop_needles(self, n):
        for i in range(n):
            self.needles.append(Needle(self.r))
        self.pi_est = self.calculate_pi_est()

    def calculate_pi_est(self):
        trials = len(self.needles)
        successes = sum([n.outcome for n in self.needles])
        p = successes / trials
        return 2 * self.r / p if p > 0 else float('inf')


class Experiments:
    def __init__(self, n_experiments, n_needles, r=1):
        self.n_experiments = n_experiments
        self.n_needles = n_needles
        self.r = r
        self.results = self.run_experiments()
        self.mean_pi_est = statistics.mean(self.results)
        self.variance_pi_est = statistics.variance(self.results)
        self.sd_pi_est = statistics.stdev(self.results)

    def run_experiments(self):
        results = []
        for i in range(self.n_experiments):
            e = Experiment(self.r)
            e.drop_needles(self.n_needles)
            results.append(e.pi_est)
        return results


 