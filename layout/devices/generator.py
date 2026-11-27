#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""GF180MCU PCell generator for OpenVLSI.

OpenVLSI invokes this script with:

    generator.py --pdk-root <package> --module pcells --class nmos \
                        --params-file params.json --output geometry.json

The actual device implementations live in ``layout/devices/pcell/pcells.py`` and use the
``openvlsipy`` layout builder API shipped with OpenVLSI.
"""

from __future__ import annotations

import sys


def main() -> int:
    try:
        from openvlsipy import pcells
    except ImportError as error:
        print(
            "The GF180MCU PCell generator requires the OpenVLSI openvlsipy Python module. "
            f"Set PYTHONPATH to the OpenVLSI Python/build directories. ({error})",
            file=sys.stderr,
        )
        return 2
    return pcells.package_main_cli()


if __name__ == "__main__":
    raise SystemExit(main())
