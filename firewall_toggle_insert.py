import keyboard
import subprocess
import os

def toggle_firewall():
    script_path = os.path.join(os.path.dirname(__file__), "firewall_toggle.ps1")
    subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", script_path])

keyboard.add_hotkey("insert", toggle_firewall)
print("Toggle ativo na tecla: Insert. Pressiona ESC para sair.")
keyboard.wait("esc")
