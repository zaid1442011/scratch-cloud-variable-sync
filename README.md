
# scratch-cloud-variable-sync

A python script to sync Scratch's cloud variables to Turbowarp's cloud server.

## Notice:

This is an experimental branch for 2-way communication between Scratch and Turbowarp.

THIS ISN'T A STABLE BRANCH YET.

## Installation

These instructions are for Unix-based operating systems only (macOS, BSD, and Linux).

1. (Recommended for end users) The first step is to download the [.zip file](https://github.com/zaid1442011/scratch-cloud-variable-sync/releases) here.  (Recommended for developers) By opening the terminal and typing:

```sh
git clone -b 2-way-communication https://github.com/zaid1442011/scratch-cloud-variable-sync.git
```

If you don't have git, [install it](https://git-scm.com/downloads) or extract the [.zip file](https://github.com/zaid1442011/scratch-cloud-variable-sync/releases) to the home folder.

2. Change directory to the repository:

```sh
cd scratch-cloud-variable-sync
```

3.  (Recommended) Make a python virtual environment
```sh
python3 -m venv .
```
And activate it (Note: You need to do this every time you deactivate the virtual environment or close the terminal session.)
```sh
source ./bin/activate
```

4. Install the required dependencies
```sh
pip3 install -r requirements.txt
```
Note: this branch uses [a custom version of scratchattach](https://github.com/zaid1442011/scratchattach) until [this pull request is merged](https://github.com/TimMcCool/scratchattach/pull/230)

5. Copy the contents off the example.env folder and create an 'app.env' text file and paste the contents of 'example.env' there. Fill the fields in the newly created 'app.env' with their respective values.

6. Start the script
```sh
python3 app.py
```

## Contributing

All contributions are welcome, but they must abide by our [contribution guidelines](https://github.com/zaid1442011/scratch-cloud-variable-sync/blob/main/CONTRIBUTING.md).

## Help

If you have any question, suggestions, or encounter any issues. File an issue [here](https://github.com/zaid1442011/scratch-cloud-variable-sync/issues).