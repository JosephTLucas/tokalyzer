import importlib
import pkgutil
import inspect


def load_rules():
    rules = []
    package = "tokalyzer.rules_dir"

    module_infos = pkgutil.iter_modules(path=["tokalyzer/rules_dir"])

    for module_info in module_infos:
        module_name = module_info.name
        try:
            module = importlib.import_module(f"{package}.{module_name}")

            for name, obj in inspect.getmembers(module):
                if inspect.isfunction(obj) or inspect.ismethod(obj):
                    rules.append(obj)
        except Exception as e:
            print(f"Error loading module {module_name}: {e}")

    return rules


if __name__ == "__main__":
    rules = load_rules()
    print(f"Loaded {len(rules)} rules.")
    for rule in rules:
        print(rule)
