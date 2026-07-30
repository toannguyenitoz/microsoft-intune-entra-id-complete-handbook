<a id="top"></a>

<!-- HANDBOOK-HEADER:START -->
<div align="center">

<img src="../assets/images/12-troubleshooting-playbook.svg" alt="🧰 Microsoft Intune Troubleshooting Playbook" width="100%" />

[![Microsoft Intune](https://img.shields.io/badge/Microsoft-Intune-0078D4?logo=microsoft&logoColor=white)](https://learn.microsoft.com/mem/intune/)
[![Microsoft Entra ID](https://img.shields.io/badge/Microsoft-Entra_ID-5C2D91?logo=microsoftazure&logoColor=white)](https://learn.microsoft.com/entra/identity/)
[![Microsoft 365](https://img.shields.io/badge/Microsoft-365-D83B01?logo=microsoftoffice&logoColor=white)](https://learn.microsoft.com/microsoft-365/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](../README.md)

[🏠 Handbook Home](../README.md) · [🧪 Labs](../labs/README.md) · [⚡ Scripts](../scripts/README.md) · [📋 Templates](../templates/README.md)

</div>
<!-- HANDBOOK-HEADER:END -->

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

<!-- HANDBOOK-FOOTER:START -->
---

<div align="center">

### 👨‍💻 Xuan Toan Nguyen

**IT Support · Systems Administration · Microsoft 365 · Azure · Modern Workplace**  
📍 Adelaide, South Australia  
🏅 Silver Medalist — WorldSkills Australia SA Regional Competition 2026, Cloud Computing

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Toan%20Nguyen-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/toan-nguyen-it-oz)
[![GitHub](https://img.shields.io/badge/GitHub-toannguyenitoz-181717?logo=github&logoColor=white)](https://github.com/toannguyenitoz)
[![Repository](https://img.shields.io/badge/Repository-Intune%20%26%20Entra%20Handbook-0078D4?logo=github&logoColor=white)](https://github.com/toannguyenitoz/microsoft-intune-entra-id-complete-handbook)

**#MicrosoftIntune · #MicrosoftEntraID · #Microsoft365 · #ModernWorkplace · #ToanNguyenITOz**

[⬆ Back to Top](#top) · [🏠 Back to Handbook](../README.md)

</div>
<!-- HANDBOOK-FOOTER:END -->
