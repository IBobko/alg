# Google Services API Integration

This project demonstrates how to interact with various Google services using Python. It includes examples for Google
Drive, Google Contacts, and Google Sheets.

## Prerequisites

Before running the code, make sure you have the following prerequisites:

- Python 3.x installed
- Google API credentials (JSON file) for the respective services
- Required Python packages installed. For this, you can use a virtual environment and install dependencies
  from `requirements.txt`.

## Setting Up the Virtual Environment

1. In your terminal window, navigate to the directory of the project.

2. Initialize a new virtual environment by running:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment. On macOS and Linux, use:

   ```bash
   source venv/bin/activate
   ```

   On Windows, use:

   ```bash
   .\venv\Scripts\activate
   ```

4. With the virtual environment activated, install the necessary dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

## Running the script

The main script can be executed via command line using the following instructions:

1. Open a terminal window and navigate to the directory containing the `main.py` file.

2. Run the command:

```bash
python main.py [command]
```

Replace `[command]` with one of the following commands depending on the operation you want to perform:

- `save_contacts`: This command saves the contacts to a Google Sheet.
- `other_command`: The functionality for this command should be added accordingly.

If an unknown command is entered, the script will notify the user about the unknown command.

Note: Ensure that you have the necessary permissions and credentials to perform these operations.
