#!/usr/bin/env zsh
set -e

if [ -n "$1" ] && [ -d "scripts/$1" ] && [ -f "scripts/$1/$1.py" ]; then
  echo "RECOGNISED SCRIPT $1"
else
  echo "ERROR: ARGUMENT MUST BE A VALID SCRIPT"
  echo "       scripts/$1/$1.mjs DOES NOT EXIST"
  exit
fi

SCRIPT=$1

echo "DEPLOYMENT WILL BEGIN\n"
echo -n "Press any key to continue, CTRL-C to exit now ...\n"
read -n 1

DEST=~/scripts/py-scripts
SRC=~/dev/py-scripts

# Sync code
rsync -a "$SRC/scripts/" "$DEST/scripts/"

python3 -m venv "$DEST/.venv"
source "$DEST/.venv/bin/activate"
pip install pip-tools
pip install -r "$SRC/requirements.txt"
if [ -f "$SRC/scripts/$SCRIPT/requirements.txt" ]; then
  pip-sync "$SRC/scripts/$SCRIPT/requirements.txt"
fi

# Replace symlink with a wrapper script
sudo rm -f /usr/local/bin/$SCRIPT

WRAPPER=/usr/local/bin/$SCRIPT

cat <<EOF | sudo tee "$WRAPPER" > /dev/null
#!/usr/bin/env bash
source "$DEST/.venv/bin/activate"
exec python "$DEST/scripts/$SCRIPT/$SCRIPT.py" "\$@"
EOF

sudo chmod +x "$WRAPPER"

echo "Deployed Python script $SCRIPT to $DEST"
