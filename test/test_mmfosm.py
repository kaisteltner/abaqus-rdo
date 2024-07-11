import unittest
import numpy as np

import abaqusrdo.calculate_derivatives as cd

class TestMMFOSM(unittest.TestCase):

    def setUp(self):
        # Three bar bracket, DV: A, RV: Fx
        mean_rv = [[-0.79788456], [0.79788456]] # 0.75, 1.5
        sigma_rv = [[0.60281028], [0.60281028]]
        delta_rv = [[0.0001], [0.0001]]
        weights = [0.5, 0.5]
        run_ids = np.reshape(range(4), (2, 2))
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
        self.dresp = cd.Dresp('tbb_compliance', list_RV, weights)
        self.dresp.value = [2.07236539, 2.07238287, 2.55374371, 2.55378656]
        self.dresp.dDV = np.asarray([[-1.00178854, -1.14714688, -0.28288283],
                                    [-1.00184204, -1.14716304, -0.28286588],
                                    [-2.03751428, -1.41941968, -0.07704459],
                                    [-2.03759059, -1.41943765, -0.07703574]])
        self.dresp.calculate_partial_derivatives()
        self.dresp.calculate_objective(cov, 1)


    def test_dRV(self):
        np.testing.assert_allclose(self.dresp.dRV, [[0.174796], [0.428522]], 1e-3)

    def test_mean(self):
        np.testing.assert_allclose(self.dresp.mean, [2.072365, 2.553744], 1e-3)

    def test_var(self):
        np.testing.assert_allclose(self.dresp.var, [0.011103, 0.066728], 1e-3)

    def test_mean_x(self):
        np.testing.assert_allclose(self.dresp.mean_x, 2.313055, 1e-3)

    def test_var_x(self):
        np.testing.assert_allclose(self.dresp.var_x, 0.096847, 1e-3)

    def test_sigma_x(self):
        np.testing.assert_allclose(self.dresp.sigma_x, 0.311202, 1e-3)

    def test_dmean_x(self):
        np.testing.assert_allclose(self.dresp.dmean_x_dDV, [-1.519651, -1.283283, -0.179964], 1e-3)

    def test_dvar_x(self):
        np.testing.assert_allclose(self.dresp.dvar_x_dDV, [-0.402091, -0.103776, 0.074086], 1e-3)

    


if __name__ == '__main__':
    unittest.main()