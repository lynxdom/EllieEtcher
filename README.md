# EllieEtcher
A simple svg to gcode converter for use in a diy laser etcher.

# install QT
sudo pacman -S qt6-base qtcreator

# Setup
git clone EllieEtcher
cd EllieEtcher
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

qtcreator pyproject.toml