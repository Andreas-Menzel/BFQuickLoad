import requests
import json
import os

def extract_openapi_spec(url: str = "http://localhost:8000/openapi.json", output_path: str = "openapi.json"):
    """
    Extracts the OpenAPI specification from a running FastAPI server and saves it to a file.

    Args:
        url (str): The URL of the OpenAPI JSON endpoint.
        output_path (str): The path to save the openapi.json file.
    """
    try:
        print(f"Attempting to fetch OpenAPI spec from: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        openapi_spec = response.json()

        # Ensure the output directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(output_path, "w") as f:
            json.dump(openapi_spec, f, indent=2)
        print(f"OpenAPI spec successfully saved to: {output_path}")

    except requests.exceptions.ConnectionError:
        print(f"Error: Could not connect to the FastAPI server at {url}. "
              "Please ensure the server is running and accessible.")
    except requests.exceptions.Timeout:
        print(f"Error: Request timed out while trying to reach {url}. "
              "The server might be slow or unresponsive.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred: {e}")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the response. "
              "The server might not be returning a valid OpenAPI JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # You might need to change the URL if your FastAPI server runs on a different host/port
    # or if the openapi.json endpoint is different.
    extract_openapi_spec()
