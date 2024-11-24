
# **Animal Web Generator**

This project dynamically generates a website that displays information about animals. It fetches data from the [API Ninjas Animals API](https://api-ninjas.com/) and creates an HTML webpage with details about the selected animal.

---

## **Project Description**

The **Animal Web Generator** allows users to input an animal name, fetches relevant data from the API, and generates a webpage (`animals.html`) displaying the animal's characteristics. This project demonstrates modular programming by separating data fetching and website generation into distinct components.

### **Features**
- Fetches animal data dynamically using the API Ninjas Animals API.
- Generates a clean and structured HTML webpage.
- Modular architecture for maintainability and scalability.

---

## **Technologies Used**
- Python
- HTML
- [API Ninjas Animals API](https://api-ninjas.com/)
- dotenv for environment variable management

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your API key:
   ```plaintext
   API_KEY=your_api_key_here
   ```

---

## **Usage**

1. Run the `animals_web_generator.py` script:
   ```bash
   python animals_web_generator.py
   ```
2. Enter the name of an animal when prompted.
3. The program will fetch data from the API and generate a webpage (`animals.html`) in the root directory.
4. Open `animals.html` in your browser to view the generated webpage.

---

## **File Structure**

- **`animals_web_generator.py`**: Handles website generation by serializing animal data into HTML.
- **`data_fetcher.py`**: Fetches animal data from the API.
- **`animals_template.html`**: HTML template used to generate the final webpage.
- **`requirements.txt`**: Lists all dependencies required for the project.

---



### **Dependencies**
The following dependencies are required to run this project (as listed in `requirements.txt`):
- `requests`
- `os`
- `dotenv`




