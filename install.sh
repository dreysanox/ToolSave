#!/bin/bash

# Check for python3
if ! command -v python3 &> /dev/null; then
    echo "python3 could not be found. Please install python3 to continue."
    exit 1
fi

SCRIPT_DIR=$(dirname $(realpath $0))

# Define the name for the command
COMMAND_NAME="toolsave"

# Create a wrapper script in /bin
WRAPPER_SCRIPT="/bin/$COMMAND_NAME"
echo "#!/bin/bash" > $WRAPPER_SCRIPT
echo "cd $SCRIPT_DIR && python3 main.py && cd -" >> $WRAPPER_SCRIPT

# Make the wrapper script executable
chmod +x $WRAPPER_SCRIPT

echo "Installation complete. You can now use ToolSave by typing '$COMMAND_NAME' in your terminal."

