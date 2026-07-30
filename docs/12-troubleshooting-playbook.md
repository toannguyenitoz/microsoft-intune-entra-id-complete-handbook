# 🧰 Microsoft Intune Troubleshooting Playbook

[🏠 Home](../README.md)

## Standard Investigation Flow

```text
Identify affected user/device
→ Confirm licence and service health
→ Confirm Entra and Intune objects
→ Check ownership and primary user
→ Review group membership and filters
→ Check policy/app assignment
→ Force sync and note timestamp
→ Review portal error code
→ Collect local logs
→ Reproduce and validate fix
→ Record root cause and prevention
```

## Force a Device Sync

From Windows:

```text
Settings → Accounts → Access work or school
→ Select connected account → Info → Sync
```

From Company Portal:

```text
Settings → Sync
```

## Useful Commands

```powershell
# Join and registration status
dsregcmd /status

# MDM enrollment tasks
Get-ScheduledTask -TaskPath '\Microsoft\Windows\EnterpriseMgmt\'

# Intune Management Extension service
Get-Service IntuneManagementExtension

# Device certificate overview
Get-ChildItem Cert:\LocalMachine\My

# Recent MDM events
Get-WinEvent -LogName 'Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider/Admin' -MaxEvents 50
```

## Common Scenarios

### Device does not appear in Intune

Check licence, MDM scope, enrollment restriction, Entra join state, device limit, network access, and MDM event logs.

### Policy remains Pending

Confirm assignment, group membership, filters, applicability, last check-in time, conflicting profiles, and supported Windows edition.

### Win32 app fails

Test the command as SYSTEM, verify requirements and detection, inspect IME logs, check dependencies, and confirm exit codes.

### Device is noncompliant

Open the per-setting compliance report, allow evaluation time, validate encryption and security services locally, and check whether a grace period expired.

### Conditional Access blocks a valid user

Use the Entra sign-in log's Conditional Access tab, inspect applied policies, confirm device ID and compliance claim, and use the What If tool before changing policy.

### Duplicate device objects

Compare device ID, Entra device ID, serial number, ownership, enrollment date, and last check-in before removing stale records.

## Escalation Evidence Checklist

- [ ] User principal name
- [ ] Device name and serial number
- [ ] Entra device ID
- [ ] Intune device ID
- [ ] Time and timezone of failure
- [ ] Screenshot and exact error code
- [ ] Assignment and group details
- [ ] Last successful sync
- [ ] Relevant log bundle
- [ ] Troubleshooting actions already completed

> [!IMPORTANT]
> Avoid deleting and re-enrolling a device as the first troubleshooting step. Capture evidence first, because re-enrollment can remove the state needed to identify the root cause.
