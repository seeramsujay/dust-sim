import json
from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parent.parent

def test_package_json():
    pkg_file = REPO_ROOT / "package.json"
    assert pkg_file.exists(), "package.json should exist"
    data = json.loads(pkg_file.read_text())
    assert data["name"] == "dust-vision-sim"
    assert "build" in data["scripts"]
    assert "react" in data["dependencies"]
    assert "@react-three/fiber" in data["dependencies"]
    assert "three" in data["dependencies"]

def test_dust_sim_jsx_constants():
    component_file = REPO_ROOT / "src" / "components" / "dust-sim.jsx"
    assert component_file.exists(), "dust-sim.jsx should exist"
    content = component_file.read_text()
    for state in ["NORMAL", "MONITOR", "WARNING", "PREDICTIVE", "MITIGATION", "ERROR"]:
        assert state in content, f"State {state} should be defined in dust-sim.jsx"

def test_vercel_config():
    vercel_file = REPO_ROOT / "vercel.json"
    if vercel_file.exists():
        data = json.loads(vercel_file.read_text())
        assert isinstance(data, dict)
