import keyboard
import subprocess
import tempfile

ps1_data = """
$adapters = Get-NetAdapter | Where-Object { $_.Status -eq 'Up' -or $_.Status -eq 'Disabled' }
$enabled = $adapters | Where-Object { $_.Status -eq 'Up' }

if ($enabled.Count -gt 0) {
    $enabled | ForEach-Object {
        Disable-NetAdapter -Name $_.Name -Confirm:$false
    }
    Start-Sleep -Seconds 1
    $count = ($enabled).Count
    Write-Host "[✔] Toggle desativado: $count adaptador(es) BLOQUEADO(S)"
} else {
    $adapters | ForEach-Object {
        Enable-NetAdapter -Name $_.Name -Confirm:$false
    }
    Start-Sleep -Seconds 1
    $count = ($adapters).Count
    Write-Host "[✔] Toggle ativado: $count adaptador(es) REATIVADO(S)"
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
