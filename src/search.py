import requests
import datetime
import logging

def query(query_string: str, api_host: str, token: str, context=None) -> str:
    """
    Python equivalent of the Go query function.
    
    Args:
        query_string: The query string to send to the API
        api_host: The base URL of the API
        token: The authentication token
        context: Optional context (not used in this implementation)
        
    Returns:
        The response body as a string
        
    Raises:
        Exception: If the request fails or returns a non-200 status code
    """
    # Construct the endpoint URL
    endpoint_url = f"{api_host}/gpt/email/query"
    
    # Add query parameters
    params = {
        'q': query_string,
        't': datetime.datetime.now().astimezone().isoformat()
    }
    
    # Add Authorization header
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    try:
        # Perform the request
        response = requests.get(endpoint_url, params=params, headers=headers)
        
        # Check status code
        if response.status_code != 200:
            error_msg = f"Unexpected status code: {response.status_code}"
            logging.error(error_msg)
            raise Exception(error_msg)
        
        # Return the response body
        return response.text
    
    except requests.RequestException as e:
        error_msg = f"Failed to execute request: {str(e)}"
        logging.error(error_msg)
        raise Exception(error_msg)
    
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        logging.error(error_msg)
        raise