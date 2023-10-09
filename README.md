## Usage
The GPT-Cookbook API provides endpoints to interact with the recipe database. Below are the primary actions that can be performed:

### Submit GPT-Generated Recipes
Clients can submit new recipes by sending a `POST` request with a JSON body containing the GPT-generated recipe.

- **Endpoint:** `POST /api/recipes`
- **Payload:** JSON object containing the GPT-generated recipe.
- **Example Payload:**
  ```json
  {
    "title": "GPT's Delicious Pancakes",
    "ingredients": [
      {
        "item": "flour",
        "quantity": "1 cup"
      },
      // ... Other ingredients ...
    ],
    "steps": [
      "In a large bowl, mix together the flour, salt, and baking powder.",
      // ... Other steps ...
    ],
    // ... Any other recipe fields ...
  }



### Notes:
- Ensure you provide examples of the expected JSON format and structure that your API will accept.
- Clearly document any validation rules or constraints on the JSON payloads.
- Explain how the API will respond to these `POST` requests, including the format of the response, any status codes returned, and how errors are handled.
  
With these updates, clients of your API will have clear instructions on how to submit GPT-generated recipe JSON bodies and what to expect in response. Adjust and expand upon these examples to match the exact behavior and requirements of your API.
