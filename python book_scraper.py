import requests
from bs4 import BeautifulSoup # type: ignore
import pandas as pd


URL = "http://books.toscrape.com/catalogue/page-{}.html"

def scrape_books(page_number):
    """Scrape book information from a given page number."""
    url = URL.format(page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    books = []
    book_elements = soup.find_all("article", class_="product_pod")

    for book in book_elements:
    
        title = book.h3.a["title"]

    
        price = book.find("p", class_="price_color").text[2:]

        
        rating = book.find("p", class_="star-rating")["class"][1]

        books.append({"Title": title, "Price": price, "Rating": rating})

    return books

def scrape_all_books():
    """Scrape all books across multiple pages."""
    all_books = []

    
    for page_number in range(1, 51):
        print(f"Scraping page {page_number}...")
        books = scrape_books(page_number)
        all_books.extend(books)

    return all_books

def save_to_csv(data, filename):
    """Save scraped data to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    all_books = scrape_all_books()
    save_to_csv(all_books, "books.csv")

if __name__ == "__main__":
    main()
