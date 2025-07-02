$adapterName = "Ethernet"  # Altera para "Wi-Fi" se necessário
$state = Get-NetAdapter -Name $adapterName | Select-Object -ExpandProperty Status

if ($state -eq "Up") {
    Disable-NetAdapter -Name $adapterName -Confirm:$false
    Write-Host "Internet OFF"
} else {
    Enable-NetAdapter -Name $adapterName -Confirm:$false
    Write-Host "Internet ON"
}
