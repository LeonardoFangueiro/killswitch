import keyboard
import subprocess
import tempfile

ps1_data = """
$adapterName = "Ethernet"
$state = Get-NetAdapter -Name $adapterName | Select-Object -ExpandProperty Status

if ($state -eq "Up") {
    Disable-NetAdapter -Name $adapterName -Confirm:$false
    Write-Host "Internet OFF"
} else {
    Enable-NetAdapter -Name $adapterName -Confirm:$false
    Write-Host "Internet ON"
}
"""

def toggle_firewall():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".ps1", mode='w', encoding='utf-8') as tmpfile:
        tmpfile.write(ps1_data)
        tmpfile_path = tmpfile.name
    subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", tmpfile_path])

keyboard.add_hotkey("insert", toggle_firewall)
print("Toggle ativo na tecla: Insert. Pressiona ESC para sair.")
keyboard.wait("esc")
