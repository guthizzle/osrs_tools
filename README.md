# OSRS Combat Metrics Tools

## Overview

OSRS Combat Metrics Tools is a Python suite for analysing and comparing combat-related metrics in Old School RuneScape (OSRS).

The toolkit is designed to help players, theorycrafters, and developers evaluate the effectiveness of various mechanics, current focus is combat orientated.

While the project aims to support a wide range of combat calculations, the currently implemented tool is the `DpsSpec` class for special attack analysis.

## Features

- **Extensible Toolkit**: Designed to support a broad range of combat metric calculations.
- **Special Attack Analysis**: Calculate DPS, efficiency, time to kill, and time saved for special attacks.
- **Easy Integration**: Modular structure for future expansion (e.g., accuracy, expected hit, gear comparison).

## Installation

Clone the repository

Install dependencies with:

```
pip install -r requirements.txt
```

## Usage Examples

### Dps Specs

```python
from specs.dps_spec import DpsSpec

# Initialise a special attack spec
spec = DpsSpec(spec_dps=100.0, spec_dmg=200.0, attack_speed=2.0, spec_cost=50)
spec.set_target(target_hitpoints=1000.0, main_dps=50.0)

print("Time to kill:", spec.ttk)
print("Spec efficiency:", spec.spec_efficiency)
print("Time saved:", spec.spec_time_save)
print("Time save efficiency:", spec.spec_time_save_efficiency)
```

## Project Structure

```
.
├── main.py
├── requirements.txt
├── specs/
│   ├── __init__.py
│   └── dps_spec.py
└── .gitignore
```

## Testing

Unit tests can be added in a `tests/` directory. To run tests (once implemented):

```
pytest
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for new features, bug fixes, or suggestions for additional combat metric tools.

## License

MIT License. See the LICENSE file for details.
