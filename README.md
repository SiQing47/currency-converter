# Currency Conversion API

This is a simple Flask-based API that performs currency conversion using provided exchange rates.

## How to Run

1. Install Flask (if not already installed):

```bash
pip install Flask

```

2. Run the API:
```bash
python app.py
```

## Usage
Make a GET request to /convert with the following query parameters:

- `source`: Source currency code (default: USD)
- `target`: Target currency code (default: USD)
- `amount`: Amount to convert (e.g., $1,525)

Example:
```bash
GET /convert?source=USD&target=JPY&amount=$1,525
```

Response: 
```json
{
  "msg": "success",
  "amount": "$170,496.53"
}
```

## Unit Tests

To run unit tests, you can use the following command:

```bash
python test_app.py
```