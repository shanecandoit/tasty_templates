# Tasty Templates

This project uses Jinja2 templates to generate code from a YAML definition file.

The `definitions.yaml` file defines data types and functions. The Jinja2 templates in the `templates/` directory are used to generate code in different languages based on the definitions in the YAML file.

The `generate_templates.py` script reads the `definitions.yaml` file and uses the Jinja2 templates to generate code in the `generated_templates/` directory.

The `test_generate_templates.py` script contains tests to verify that the generated code is correct.
