# Django Flutterwave

## Project Description

This project provides Django integration for [Flutterwave](https://flutterwave.com/) payments and subscriptions.

Current functionality:
- Allow users to make payments (once off and subscription)
- Create payment buttons which launch inline payment modals
- Maintain a payment transaction history linked to users

# Requirements

- Python >= 3.6
- Django >= 2.0

# Installation

```bash
pip install djangoflutterwave
```

# Setup

Add `"flutterwave"` to your `INSTALLED_APPS`

Run Django migrations:

```python
manage.py migrate
```

Add the following to your `settings.py`:

```python
FLW_PRODUCTION_PUBLIC_KEY = "your key"
FLW_PRODUCTION_SECRET_KEY = "your key"
FLW_SANDBOX_PUBLIC_KEY = "your key"
FLW_SANDBOX_SECRET_KEY = "your key"
FLW_SANDBOX = True
```

The above config will ensure `flutterwave` uses your sandbox. Once you're ready to
go live, set `FLW_SANDBOX = False`


```

