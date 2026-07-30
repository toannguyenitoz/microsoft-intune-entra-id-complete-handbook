<a id="top"></a>

<!-- HANDBOOK-HEADER:START -->
<div align="center">

<img src="../assets/images/10-windows-autopilot.svg" alt="🚀 Windows Autopilot Deployment" width="100%" />

[![Microsoft Intune](https://img.shields.io/badge/Microsoft-Intune-0078D4?logo=microsoft&logoColor=white)](https://learn.microsoft.com/mem/intune/)
[![Microsoft Entra ID](https://img.shields.io/badge/Microsoft-Entra_ID-5C2D91?logo=microsoftazure&logoColor=white)](https://learn.microsoft.com/entra/identity/)
[![Microsoft 365](https://img.shields.io/badge/Microsoft-365-D83B01?logo=microsoftoffice&logoColor=white)](https://learn.microsoft.com/microsoft-365/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](../README.md)

[🏠 Handbook Home](../README.md) · [🧪 Labs](../labs/README.md) · [⚡ Scripts](../scripts/README.md) · [📋 Templates](../templates/README.md)

</div>
<!-- HANDBOOK-HEADER:END -->

# 🚀 Windows Autopilot Deployment

[🏠 Home](../README.md)

## Deployment Workflow

1. Confirm licensing and Windows edition.
2. Register the device hardware hash or use OEM registration.
3. Create a dynamic Autopilot device group.
4. Create and assign a deployment profile.
5. Configure Enrollment Status Page.
6. Assign required applications and security policies.
7. Start the device in OOBE and connect to the internet.
8. Sign in with the assigned user.
9. Validate Entra join, Intune enrollment, compliance, apps, and updates.

## Example Dynamic Group Rule

```text
(device.devicePhysicalIDs -any (_ -startsWith "[ZTDId]"))
```

## Recommended Pilot Controls

- User-driven Entra join
- Standard user account
- Skip privacy settings where approved
- Hide change-account options
- Block device use until required policies and apps complete
- Use a dedicated Autopilot pilot group

## Troubleshooting Checklist

- [ ] Device appears under Windows Autopilot devices
- [ ] Profile status is Assigned
- [ ] User has an Intune licence
- [ ] Enrollment restrictions permit Windows enrollment
- [ ] Network can reach required Microsoft endpoints
- [ ] TPM and device time are healthy
- [ ] Enrollment Status Page has not timed out
- [ ] Required app detection rules are correct

Useful command during diagnostics:

```powershell
Get-AutopilotDiagnostics.ps1 -Online
```

> [!TIP]
> A single incorrectly packaged required Win32 app can block the entire Enrollment Status Page. Test required apps independently before adding them to Autopilot.

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
