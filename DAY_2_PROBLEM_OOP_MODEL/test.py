import unittest
from DAY_2_PROBLEM_OOP_MODEL.program import Disease, Cancer


class DiseaseTest(unittest.TestCase):

    # Setup test suite: Disease object instantiated with prevalence of 20% and survival_rate of 40%
    def setUp(self):
        self.disease = Disease(20, 40)

    # First test: Method called infected returns number of infected people
    def test_infected_method(self):
        self.assertEqual(self.disease.infected(5000), 1000, msg="infected method in Disease class returns wrong values")

    # Second test: Method called survive returns number of survivors
    def test_survive_method(self):
        self.assertEqual(self.disease.survive(5000), 400, msg="survive method in Disease class returns wrong values")

    # Third test: Method called death returns number of deaths
    def test_death_method(self):
        self.assertEqual(self.disease.death(5000), 600, msg="death method in Disease class returns wrong values")


class CancerTest(unittest.TestCase):

    # Setup test suite: Cancer object instantiated with prevalence of 20% and survival_rate of 40%
    def setUp(self):
        self.cancer1 = Cancer(True)
        self.cancer2 = Cancer(False)

    # First test: Method called infected returns number of infected people
    def test_infected_method(self):
        self.assertEqual(self.cancer1.infected(10000), 4500, msg="infected method in Cancer class returns wrong values for terminal=True")
        self.assertEqual(self.cancer2.infected(10000), 4500, msg="infected method in Cancer class returns wrong values for terminal=False")

    # Second test: Method called survive returns number of survivors
    def test_survive_method(self):
        self.assertEqual(self.cancer1.survive(10000), 0, msg="survive method in Cancer class returns wrong values for terminal=True")
        self.assertEqual(self.cancer2.survive(10000), 3150, msg="survive method in Cancer class returns wrong values for terminal=False")

    # Third test: Method called death returns number of deaths
    def test_death_method(self):
        self.assertEqual(self.cancer1.death(10000), 4500, msg="death method in Cancer class returns wrong values terminal=True")
        self.assertEqual(self.cancer2.death(10000), 1350, msg="death method in Cancer class returns wrong values for terminal=False")

if __name__ == '__main__':
    unittest.main()