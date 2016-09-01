"""
<example>
"""

import teetool as tt  # core
from teetool import visual_2d

# parameters
ntraj = 50
ndim = 2

# build world
new_world = tt.World(name="Example 2D", ndim=ndim)

# modify default resolution
new_world.setResolution(xstep=50, ystep=50)

# add trajectories
for ntype in [0, 1]:
    cluster_name = "toy {0}".format(ntype)
    cluster_data = tt.helpers.get_trajectories(ntype, ndim, ntraj)
    new_world.addCluster(cluster_data, cluster_name)

# overview
new_world.overview()

# model all trajectories
settings = {}
settings["model_type"] = "resample"
settings["ngaus"] = 100

settings["model_type"] = "ML"
settings["ngaus"] = 100
settings["basis_type"] = "rbf"
settings["nbasis"] = 50

new_world.buildModel(0, settings)
new_world.overview()  # overview
new_world.buildModel(1, settings)
new_world.overview()  # overview

new_world.buildLogProbality(0)
new_world.overview()  # overview
new_world.buildLogProbality(1)
new_world.overview()  # overview

for i in [0, 1]:
    # visuals by mayavi
    visual = visual_2d.Visual_2d(new_world)
    # visualise trajectories
    visual.plotTrajectories([i])
    # visualise intersection
    visual.plotLogProbability([i])

# visuals by mayavi
visual = visual_2d.Visual_2d(new_world)
# visualise trajectories
visual.plotTrajectories([0, 1])
# visualise intersection
visual.plotLogProbability([0, 1])

# show [ requires user input ]
visual.show()
