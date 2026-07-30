# 📦 Win32 Application Packaging

[🏠 Home](../README.md)

## 1. Prepare the Source Folder

```text
C:\IntuneApps\7-Zip\Source
C:\IntuneApps\7-Zip\Output
```

Keep only required installer files in the source folder. Remove logs, screenshots, and unrelated files.

## 2. Test Silent Installation Locally

```powershell
Start-Process msiexec.exe -ArgumentList '/i "7z.msi" /qn /norestart' -Wait -PassThru
```

Record the exit code and verify application functionality.

## 3. Package the Application

```powershell
IntuneWinAppUtil.exe `
  -c "C:\IntuneApps\7-Zip\Source" `
  -s "7z.msi" `
  -o "C:\IntuneApps\7-Zip\Output" `
  -q
```

## 4. Configure the Intune Application

**Portal path:** `Apps → Windows → Add → Windows app (Win32)`

Configure:

- Name, publisher, version, owner, and notes
- Install and uninstall commands
- System or user install context
- Restart behaviour
- Architecture and minimum OS requirements
- Detection rules
- Dependencies
- Supersedence
- Assignments

## 5. Detection Rule Examples

### MSI product code

Use the MSI product code automatically detected by Intune.

### File detection

```text
Path: C:\Program Files\7-Zip
File: 7zFM.exe
Detection: File or folder exists
```

### Registry detection

```text
Key path: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\7-Zip
Value name: DisplayVersion
Operator: Version greater than or equal to
```

## 6. Assignment Strategy

| Assignment | Recommended Use |
|---|---|
| Required | Mandatory corporate applications |
| Available for enrolled devices | Optional apps in Company Portal |
| Uninstall | Controlled application removal |

Start with a pilot device group and confirm install, update, uninstall, and reinstallation behaviour.

## 7. Troubleshooting

Review:

```text
C:\ProgramData\Microsoft\IntuneManagementExtension\Logs\IntuneManagementExtension.log
C:\ProgramData\Microsoft\IntuneManagementExtension\Logs\AppWorkload.log
C:\ProgramData\Microsoft\IntuneManagementExtension\Logs\AgentExecutor.log
```

Common causes:

- Incorrect silent switches
- Detection rule already reports Installed
- Requirement rule excludes the device
- Installer needs a user session but runs as SYSTEM
- Pending reboot
- Dependency failure
- Installer returns an unsupported exit code

## Packaging Checklist

- [ ] Silent install succeeds locally
- [ ] Silent uninstall succeeds locally
- [ ] Exit codes documented
- [ ] Detection rule tested before upload
- [ ] Install context is correct
- [ ] Pilot assignment configured
- [ ] Logs reviewed after deployment
- [ ] Production rollout approved
