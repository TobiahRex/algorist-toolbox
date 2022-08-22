#!/usr/bin/env sh

echo "Building virtual environment"
virtualenv -p python3 env
echo "Activating virtual environment"
source env/bin/activate
echo "installing ipykernel..."
pip install -r ./requirements.txt
echo "Attaching kernel as 'algorist-toolbox'"
python3 -m ipykernel install --name algorist-toolbox --display-name "algorist-toolbox" --prefix $PWD