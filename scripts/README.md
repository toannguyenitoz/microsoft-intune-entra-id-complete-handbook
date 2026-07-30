# ⚡ PowerShell Scripts

[🏠 Home](../README.md)

This folder contains starter scripts for local Intune and Entra troubleshooting.

## Included Scripts

| Script | Purpose |
|---|---|
| `Get-IntuneDeviceDiagnostics.ps1` | Collect join, enrollment, service, event, and IME log information |
| `Test-IntunePrerequisites.ps1` | Validate common local prerequisites before escalation |

## Usage

Run PowerShell as Administrator:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\Get-IntuneDeviceDiagnostics.ps1 -OutputFolder C:\Temp\IntuneDiagnostics
```

> [!WARNING]
> Review diagnostic output before sharing it. Logs can contain usernames, tenant identifiers, device identifiers, application names, and other organizational information.
