import crud
from models import Preset
from database import create_db_and_tables

def seed_db():
    create_db_and_tables()
    presets = [
        Preset(name="Get Version", description="Displays the Betaflight firmware version.", tags=["info", "diagnostics"], content="version", author="BFQuickLoad"),
        Preset(name="Dump All Settings", description="Dumps all current Betaflight settings to the CLI.", tags=["backup", "settings"], content="dump", author="BFQuickLoad"),
        Preset(name="Dump Diff", description="Dumps only settings that differ from the default values.", tags=["backup", "settings"], content="diff", author="BFQuickLoad"),
        Preset(name="Save Settings", description="Saves current settings to permanent memory.", tags=["action", "settings"], content="save", author="BFQuickLoad"),
        Preset(name="Load Defaults", description="Loads factory default settings (requires 'save' afterwards).", tags=["action", "settings", "defaults"], content="defaults", author="BFQuickLoad"),
        Preset(name="Show PID Profile", description="Displays the active PID profile settings.", tags=["info", "tuning"], content="get pid_profile", author="BFQuickLoad"),
        Preset(name="Show Filter Settings", description="Displays all filter-related settings.", tags=["info", "filters"], content="get dterm_filter", author="BFQuickLoad"),
    ]
    for preset in presets:
        crud.create_preset(preset)
    print("Database seeded with dummy data.")

if __name__ == "__main__":
    seed_db()
