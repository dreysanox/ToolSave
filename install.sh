#!/bin/bash

# Check for python3
if ! command -v python3 &> /dev/null; then
    echo "python3 could not be found. Please install python3 to continue."
    exit 1
fi

SCRIPT_DIR=$(dirname $(realpath $0))

# Define the alias
echo "The following allias will be added to your shell for easy tool usage"
ALIAS="alias toolsave='cd $SCRIPT_DIR && python3 main.py'"
echo $ALIAS

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
        echo "Unsupported shell. Please add the following alias manually to your shell configuration file:"
        echo $ALIAS
        exit 1
        ;;
esac

# Check if the alias already exists
if grep -Fxq "$ALIAS" $SHELL_CONFIG; then
    echo "Alias already exists in $SHELL_CONFIG"
else
    echo $ALIAS >> $SHELL_CONFIG
    echo "Alias added to $SHELL_CONFIG"
fi

# Reload the shell configuration
if [ "$SHELL" = "/usr/bin/fish" ]; then
    source $SHELL_CONFIG
else
    exec $SHELL
fi

echo "Installation complete. You can now use ToolSave by typing 'toolsave' in your terminal."

