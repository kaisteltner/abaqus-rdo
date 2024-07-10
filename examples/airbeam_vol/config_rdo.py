# Provide data for random variables. All values have to be defined.
# Mean, sigma and delta have to be given per RV

number_of_rv = 2

mean_rv = [[0, 2], [-1.1284, 2], [1.1284, 2]]
sigma_rv = [[0.60281, 0.4], [0.60281, 0.4], [0.60281, 0.4]]
delta_rv = [[0.5, 0.6], [0.5, 0.6], [0.5, 0.6]]

use_central_differences = False
kappa = 3

# Flag and weights for MMFOSM
mmfosm = True
weights = [0.33, 0.33, 0.33]

# Set to true if running on windows machine, false if running on linux

run_on_windows = True

# Set to true for additional debug output

verbose = False
