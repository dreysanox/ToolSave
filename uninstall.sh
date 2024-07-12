#!/bin/bash

# Define the alias
ALIAS="alias toolsave='cd $SCRIPT_DIR && python3 main.py'"

# Determine the appropriate shell configuration file
SHELL_CONFIG=""
case "$SHELL" in
    */bash)
        SHELL_CONFIG="$HOME/.bashrc"
        ;;
    */zsh)
        SHELL_CONFIG="$HOME/.zshrc"
        ;;
    */fish)
        SHELL_CONFIG="$HOME/.config/fish/config.fish"
        ;;
    *)
        echo "Unsupported shell. Please remove the following alias manually from your shell configuration file:"
        echo $ALIAS
        exit 1
        ;;
esac

# Remove the alias from the shell configuration file
if grep -Fxq "$ALIAS" $SHELL_CONFIG; then
    sed -i "/$ALIAS/d" $SHELL_CONFIG
    echo "Alias removed from $SHELL_CONFIG"
else
    echo "Alias not found in $SHELL_CONFIG"
fi

# Reload the shell configuration
if [ "$SHELL" = "/usr/bin/fish" ]; then
    source $SHELL_CONFIG
else
    exec $SHELL
fi

# Get the directory of the current script
SCRIPT_DIR=$(dirname $(realpath $0))

# Remove the cloned repository directory
cd $SCRIPT_DIR/..
rm -rf $SCRIPT_DIR

echo "Uninstallation complete. The 'toolsave' alias has been removed and the cloned repository has been deleted."
