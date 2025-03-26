# Get the current working directory
current_directory=$(pwd)
echo "Current Directory: $current_directory"

# Change to the directory where your Python script is located
if echo "$current_directory" | grep -q "bin$"; then
    # Get the parent directory by using dirname
    parent_directory=$(dirname "$current_directory")
    echo "Parent Directory: $parent_directory"
    cd $parent_directory
fi

# Start the Python process
# $python_command $script_name
uvicorn app.main:app --host 0.0.0.0 --port 1530 --reload &
echo $! > server.pid