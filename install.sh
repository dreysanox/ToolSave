
### install.sh
```bash
#!/bin/bash

# Define the alias
echo "The following allias will be added to your shell for easy tool usage"
ALIAS="alias toolsave='python3 $(pwd)/main.py'"
echo $ALIAS

# Add the alias to the appropriate shell configuration file
SHELL_CONFIG=""
if [ -n "$BASH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
elif [ -n "$ZSH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
else
    echo "Unsupported shell. Please add the following alias manually to your shell configuration file:"
    echo $ALIAS
    exit 1
fi

# Check if the alias already exists
if grep -Fxq "$ALIAS" $SHELL_CONFIG; then
    echo "Alias already exists in $SHELL_CONFIG"
else
    echo $ALIAS >> $SHELL_CONFIG
    echo "Alias added to $SHELL_CONFIG"
fi

# Reload the shell configuration
source $SHELL_CONFIG

echo "Installation complete. You can now use ToolSave by typing 'toolsave' in your terminal."
