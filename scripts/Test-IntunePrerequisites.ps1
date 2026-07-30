[CmdletBinding()]
param()

$checks = @()

function Add-Check {
    param(
        [string]$Name,
        [bool]$Passed,
        [string]$Details
    )

    $script:checks += [pscustomobject]@{
        Check   = $Name
        Status  = if ($Passed) { 'PASS' } else { 'FAIL' }
        Details = $Details
    }
}

$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(
    [Security.Principal.WindowsBuiltInRole]::Administrator
)
Add-Check 'Running as Administrator' $isAdmin "Administrator=$isAdmin"

$os = Get-CimInstance Win32_OperatingSystem
Add-Check 'Windows detected' ($null -ne $os) $os.Caption

$dsreg = dsregcmd /status | Out-String
$joined = $dsreg -match 'AzureAdJoined\s*:\s*YES'
Add-Check 'Microsoft Entra joined' $joined 'Checked with dsregcmd /status'

$ime = Get-Service IntuneManagementExtension -ErrorAction SilentlyContinue
Add-Check 'Intune Management Extension installed' ($null -ne $ime) $(if ($ime) { "Status=$($ime.Status)" } else { 'Service not found' })

$mdmLog = Get-WinEvent -ListLog 'Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider/Admin' -ErrorAction SilentlyContinue
Add-Check 'MDM event log available' ($null -ne $mdmLog) 'DeviceManagement Enterprise Diagnostics Provider'

$loginTest = Test-NetConnection login.microsoftonline.com -Port 443 -WarningAction SilentlyContinue
Add-Check 'Microsoft sign-in endpoint reachable' $loginTest.TcpTestSucceeded 'login.microsoftonline.com:443'

$manageTest = Test-NetConnection manage.microsoft.com -Port 443 -WarningAction SilentlyContinue
Add-Check 'Intune endpoint reachable' $manageTest.TcpTestSucceeded 'manage.microsoft.com:443'

$checks | Format-Table -AutoSize

if ($checks.Status -contains 'FAIL') {
    exit 1
}

exit 0
