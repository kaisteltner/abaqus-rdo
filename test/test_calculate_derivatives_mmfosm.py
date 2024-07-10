import unittest
import numpy as np

import calculate_derivatives as cd

class TestMMFOSM(unittest.TestCase):

    def setUp(self):
        xL = 0.5
        xU = 2
        s = 1
        mL = -2/3
        mR = -1/4
        cL = 2
        cR = 1
        run_ids = np.reshape(range(4), (2, 2))
        mean_rv = [[(s + xL)/2], [(xU - s)/2]] # 0.75, 1.5
        sigma_rv = np.sqrt([[(s - xL)**2 / 12], [(xU - s) ** 2 / 12]])
        delta_rv = [[0.075], [0.15]]
        weights = [1/3, 2/3]
        list_RV = [
            [
                cd.RV(
                    i,
                    mean_rv[mode][i],
                    sigma_rv[mode][i],
                    delta_rv[mode][i],
                    False,
                    run_ids[mode][0],
                    run_ids[mode][i + 1],
                )
                for i in range(1)
            ]
            for mode in range(len(mean_rv))
        ]
        cov = cd.get_covariance(list_RV, 0)
        self.dresp = cd.Dresp('test', list_RV)
        self.dresp.value = [1.5, 1.45, 0.625, 0.5875]
        self.dresp.dDV = np.asarray([[-2/3.], [-2/3.], [-0.25], [-0.25]])
        self.dresp.calculate_partial_derivatives()
        self.dresp.calculate_objective(cov, 1, weights)


    def test_dRV(self):
        np.testing.assert_allclose(self.dresp.dRV, [[-2/3.], [-0.25]])

    def test_mean(self):
        np.testing.assert_allclose(self.dresp.mean, [1.5, 0.625])

    def test_var(self):
        np.testing.assert_allclose(self.dresp.var, [0.009259259259259, 0.005208333333333])

    def test_mean_x(self):
        np.testing.assert_allclose(self.dresp.mean_x, 0.91666666667)

    def test_var_x(self):
        np.testing.assert_allclose(self.dresp.var_x, 0.176697530864197)

    def test_sigma_x(self):
        np.testing.assert_allclose(self.dresp.sigma_x, 0.420354054178376)

    


if __name__ == '__main__':
    unittest.main()