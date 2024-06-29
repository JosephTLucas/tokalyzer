import importlib
import pkgutil
import inspect
import sys
from typing import Callable, List

def load_rules() -> List[Callable]:
    rules = []
    package_name = "tokalyzer.rules_dir"

    try:
        # Try to import the package
        rules_package = importlib.import_module(package_name)
        package_path = rules_package.__path__
    except ImportError:
        print(f"Warning: Unable to import {package_name}. Using fallback method.")
        # Fallback for development environment
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        package_path = [os.path.join(current_dir, "rules_dir")]

    for (_, module_name, _) in pkgutil.iter_modules(package_path):
        if module_name == "__init__":
            continue
        try:
            module = importlib.import_module(f"{package_name}.{module_name}")
            for name, obj in inspect.getmembers(module):
                if callable(obj) and not name.startswith("__") and obj.__module__ == module.__name__:
                    rules.append(obj)
        except Exception as e:
            print(f"Error loading module {module_name}: {e}")

    return rules

if __name__ == "__main__":
    rules = load_rules()
    print(f"Loaded {len(rules)} rules.")
    for rule in rules:
        print(f"{rule.__name__} from {rule.__module__}")