# Item keeper

Keeps items and returns them to a user.

## Features

- **Root Endpoint**: Returns a simple "hello world" message.
- **Items Endpoint**: Returns a list of items with pagination support.
- **Item by ID Endpoint**: Returns a specific item by its ID.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```
