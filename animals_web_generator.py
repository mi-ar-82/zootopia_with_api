import data_fetcher

def serialize_animal(animal_obj):
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    
    if 'characteristics' in animal_obj:
        if 'diet' in animal_obj['characteristics']:
            output += f'      <strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
        if 'locations' in animal_obj and animal_obj['locations']:
            output += f'      <strong>Location:</strong> {", ".join(animal_obj["locations"])}<br/>\n'
        if 'type' in animal_obj['characteristics']:
            output += f'      <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output

def generate_animal_cards(data):
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output

def update_html_template(template_path, output_path, animals_info):
    with open(template_path, "r") as file:
        html_content = file.read()
    updated_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    with open(output_path, "w") as file:
        file.write(updated_content)


def main():
    animal_name = input("Search an animal: ")
    
    template_file_path = "animals_template.html"
    output_file_path = "animals.html"
    try:
        animals_data = data_fetcher.fetch_data(animal_name)
        if not animals_data:
            error_message = f'<h2>The animal "{animal_name}" does not exist.</h2>'
            update_html_template(template_file_path, output_file_path, error_message)
            print(f"No data found for '{animal_name}'. A message has been added to '{output_file_path}'.")
            return
        animals_info = generate_animal_cards(animals_data)
        update_html_template(template_file_path, output_file_path, animals_info)
        print(f"HTML file generated successfully! Open '{output_file_path}' to view it.")
    
    except Exception as e:
        error_message = f'<h2>An error occurred: {e}</h2>'
        update_html_template(template_file_path, output_file_path, error_message)
        print(f"Error: {e}. A message has been added to '{output_file_path}'.")
        
if __name__ == "__main__":
    main()