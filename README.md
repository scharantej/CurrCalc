## Flask Application Design: Realtime USD to SGD Conversion
### HTML Files
- **convert.html:**
  - Contains the form for entering the USD amount and submitting it for conversion.
  - Includes a display area for showing the converted SGD amount.

### Routes
- **`/` (GET):**
  - Renders the `convert.html` template.

- **`/convert` (POST):**
  - Receives the USD amount from the form.
  - Performs the conversion to SGD based on the current exchange rate.
  - Sends the converted SGD amount back to `convert.html` for display.