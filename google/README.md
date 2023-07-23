# Google Services API Integration

This project demonstrates how to interact with various Google services using Python. It includes examples for Google
Drive, Google Contacts, and Google Sheets.

## Prerequisites

Before running the code, make sure you have the following prerequisites:

- Python 3.x installed
- Google API credentials (JSON file) for the respective services
- Required Python packages installed (see `requirements.txt`)

docs: Add numpy array reshape examples

- Added a new file "NeuralNetworks/numpy_reshape_examples.py" demonstrating different numpy array reshaping operations.
- Included examples of reshaping a one-dimensional array to a two-dimensional array, a two-dimensional array to a one-dimensional array, a two-dimensional array to a three-dimensional array, and a three-dimensional array to a two-dimensional array.

## Usage

You can run the following commands to perform specific tasks:

- To save contacts from your Google account to Google Sheets:

```shell
python ./main.py save_contacts
```

This command will fetch the contacts from your Google account and save them to a Google Sheets document.

## Troubleshooting

If you encounter any issues with Python's pip package, you can update it using the following command:

```shell
python -m ensurepip --upgrade && pip install --upgrade pip
```
Also, make sure to install the required Python packages from the requirements.txt file using the following command:
```shell
pip install -r requirements.txt
```

