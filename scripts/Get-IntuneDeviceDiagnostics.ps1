[CmdletBinding()]
param(
    [Parameter()]
    [string]$OutputFolder = "$env:PUBLIC\Documents\IntuneDiagnostics-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
)

$ErrorActionPreference = 'Continue'
New-Item -Path $OutputFolder -ItemType Directory -Force | Out-Null

function Save-CommandOutput {
    param(
        [Parameter(Mandatory)] [string]$Name,
        [Parameter(Mandatory)] [scriptblock]$Command
    )

    $path = Join-Path $OutputFolder "$Name.txt"
    try {
        & $Command 2>&1 | Out-File -FilePath $path -Encoding utf8 -Width 300
    }
    catch {
        "ERROR: $($_.Exception.Message)" | Out-File -FilePath $path -Encoding utf8
    }
}

Save-CommandOutput -Name 'ComputerInfo' -Command { Get-ComputerInfo }
Save-CommandOutput -Name 'DsRegCmd-Status' -Command { dsregcmd /status }
Save-CommandOutput -Name 'IntuneManagementExtension-Service' -Command { Get-Service IntuneManagementExtension }
Save-CommandOutput -Name 'EnterpriseMgmt-ScheduledTasks' -Command {
    Get-ScheduledTask -TaskPath '\Microsoft\Windows\EnterpriseMgmt\' | Format-List *
}
Save-CommandOutput -Name 'MDM-Events' -Command {
    Get-WinEvent -LogName 'Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider/Admin' -MaxEvents 200 |
        Select-Object TimeCreated, Id, LevelDisplayName, Message
}
Save-CommandOutput -Name 'Certificates-LocalMachine-My' -Command {
    Get-ChildItem Cert:\LocalMachine\My | Select-Object Subject, Issuer, Thumbprint, NotBefore, NotAfter
}
Save-CommandOutput -Name 'Network' -Command {
    Get-NetIPConfiguration
    Test-NetConnection login.microsoftonline.com -Port 443
    Test-NetConnection manage.microsoft.com -Port 443
}

$imeLogPath = 'C:\ProgramData\Microsoft\IntuneManagementExtension\Logs'
if (Test-Path $imeLogPath) {
    Copy-Item -Path $imeLogPath -Destination (Join-Path $OutputFolder 'IME-Logs') -Recurse -Force
}

$summary = [ordered]@{
    ComputerName = $env:COMPUTERNAME
    UserName     = $env:USERNAME
    CollectedAt  = (Get-Date).ToString('o')
    OutputFolder = $OutputFolder
}

$summary | ConvertTo-Json | Out-File (Join-Path $OutputFolder 'Summary.json') -Encoding utf8

Write-Host "Diagnostics collected at: $OutputFolder" -ForegroundColor Green
