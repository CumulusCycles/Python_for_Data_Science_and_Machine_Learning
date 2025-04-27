import requests
from bs4 import BeautifulSoup

def get_certifications_section(url):
  """
  Scrapes a webpage and finds the <section> element with the id "certifications".

  Args:
    url: The URL of the webpage to scrape.

  Returns:
    The <section> element with the id "certifications", or None if not found.
  """
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('section', {'id': 'certifications'})
  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    return None

if __name__ == '__main__':
  target_url = "https://www.cumuluscycles.com/"
  certifications_section = get_certifications_section(target_url)

  if certifications_section:
    print("Certifications section found:")
    # You can now work with the certifications_section element (e.g., extract its content)
    print(certifications_section)
    with open('certs.html', 'w', encoding='utf-8') as file:
        file.write(str(certifications_section))
    print("Certifications section written to certs.html")
  else:
    print("Certifications section not found.")