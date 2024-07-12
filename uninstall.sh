#!/bin/bash

# Define the alias
ALIAS="alias toolsave='python3 $(pwd)/main.py'"

# Determine the appropriate shell configuration file
SHELL_CONFIG=""
if [ -n "$BASH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
elif [ -n "$ZSH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
else
    echo "Unsupported shell. Please remove the following alias manually from your shell configuration file:"
    echo $ALIAS
    exit 1
fi

# Remove the alias from the shell configuration file
if grep -Fxq "$ALIAS" $SHELL_CONFIG; then
    sed -i "/$ALIAS/d" $SHELL_CONFIG
    echo "Alias removed from $SHELL_CONFIG"
else
    echo "Alias not found in $SHELL_CONFIG"
fi

# Reload the shell configuration
source $SHELL_CONFIG

# Get the directory of the current script
SCRIPT_DIR=$(dirname $(realpath $0))

# Remove the cloned repository directory
cd $SCRIPT_DIR/..
rm -rf $SCRIPT_DIR

echo "Uninstallation complete. The 'toolsave' alias has been removed and the cloned repository has been deleted."
