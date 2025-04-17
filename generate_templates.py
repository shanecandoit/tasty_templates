import yaml
import argparse
import os
from jinja2 import Environment, FileSystemLoader

def process_template(template_path, definitions, output_dir, class_name_base):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template_file = os.path.basename(template_path)
    language = template_file.split('.')[0]
    template = env.get_template(template_file)
    output_content = ""
    output_file_path = ""

    likely_class_name = os.path.splitext(os.path.basename(class_name_base))[0].capitalize()
    likely_class_name = likely_class_name.replace("-", "_").replace(" ", "_")
    
    if language == 'cpp':
        output_content = template.render(definitions=definitions)
        output_file_path = os.path.join(output_dir, likely_class_name+".h")
    elif language == 'haskell':
        output_content = template.render(definitions=definitions)
        output_file_path = os.path.join(output_dir, likely_class_name+".hs")
    elif language == 'java':
        # For Java, we might want a class name based on the input YAML
        output_content = template.render(definitions=definitions, class_name=likely_class_name)
        output_file_path = os.path.join(output_dir, f"{likely_class_name}.java")
    elif language == 'python':
        output_content = template.render(definitions=definitions)
        output_file_path = os.path.join(output_dir, "definitions.py")
    else:
        print(f"Unknown template language: {language}")
        return

    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(output_file_path, 'w') as outfile:
            outfile.write(output_content)
        print(f"{language.capitalize()} template written to: {output_file_path}")
    except IOError as e:
        print(f"Error writing {language} template to file: {e}")


if __name__ == "__main__":
    
    # Dont use argparse for now, just hardcode the paths
    # parser = argparse.ArgumentParser(description="Generate code templates from YAML definitions.")
    # parser.add_argument("input_yaml", help="Path to the input YAML file containing definitions.")
    # parser.add_argument("output_dir", help="Directory to save the generated templates.")
    # args = parser.parse_args()

    output_dir = "generated_templates"
    input_yaml = "definitions.yaml"

    # Load the YAML file
    with open(input_yaml, "r") as f:
        definitions = yaml.safe_load(f)

    # Process each template
    template_paths = ["templates/cpp.j2", "templates/haskell.j2", "templates/java.j2", "templates/python.j2"]
    for template_path in template_paths:
        process_template(template_path, definitions, output_dir, input_yaml)
        print(f"Processed template: {template_path} -> {output_dir}")