[![Travis CI](https://travis-ci.org/WillemEerland/teetool.svg?branch=master)](https://travis-ci.org/WillemEerland/teetool)

# teetool
a package to support with the statistical analysis of trajectory data -- helpful at determining the probability of clusters (collection) of trajectories colliding

purely spatial, ignores temporal effects

documentation is available at https://willemeerland.github.io/teetool/

# setup the environment in Linux

conda create -n teetool python=2.7 pytest pytest-cov mayavi numpy scipy

source activate teetool

pip install matplotlib nbval

python setup.py install

# run tests (including coverage report)

(cd test ; py.test -v --cov-report html --cov=teetool)

# jupyter notebook

Examples included in example/ folder

* requires jupyter notebook

conda install jupyter

jupyter notebook

* find example/ in browser and run files in order
