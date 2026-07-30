<a id="top"></a>

<!-- HANDBOOK-HEADER:START -->
<div align="center">

<img src="../assets/images/05-intune-activation-enrollment.svg" alt="⚙️ Intune Activation, Auto Enrollment & Restrictions" width="100%" />

[![Microsoft Intune](https://img.shields.io/badge/Microsoft-Intune-0078D4?logo=microsoft&logoColor=white)](https://learn.microsoft.com/mem/intune/)
[![Microsoft Entra ID](https://img.shields.io/badge/Microsoft-Entra_ID-5C2D91?logo=microsoftazure&logoColor=white)](https://learn.microsoft.com/entra/identity/)
[![Microsoft 365](https://img.shields.io/badge/Microsoft-365-D83B01?logo=microsoftoffice&logoColor=white)](https://learn.microsoft.com/microsoft-365/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](../README.md)

[🏠 Handbook Home](../README.md) · [🧪 Labs](../labs/README.md) · [⚡ Scripts](../scripts/README.md) · [📋 Templates](../templates/README.md)

</div>
<!-- HANDBOOK-HEADER:END -->

# ⚙️ Intune Activation, Auto Enrollment & Restrictions

[⬅ Previous](04-identity-authentication-hybrid.md) · [🏠 Home](../README.md) · [Next ➡](06-device-enrollment-methods.md)

---

## Verify Tenant Status

1. Open **Microsoft Intune Admin Center**.
2. Go to **Tenant administration → Tenant status**.
3. Confirm the service is active.
4. Confirm Microsoft Intune is the MDM authority.
5. Review connector and service health information.

## Enable Automatic Enrollment

**Portal path:** `Devices → Enrollment → Windows → Automatic enrollment`

Configure:

- **MDM user scope:** Pilot group first, then All when validated
- **MAM user scope:** Configure only when app protection enrollment scenarios require it
- Default discovery and compliance URLs unless a documented design requires changes

## Create Target Groups

| Group | Purpose |
|---|---|
| Licensed Users | Users with Intune entitlement |
| Pilot Users | Controlled enrollment testing |
| Windows Devices | Windows policy targeting |
| Compliance Pilot | Compliance validation |
| App Deployment Pilot | Application testing |
| Update Ring Pilot | Windows update testing |

## Enrollment Restrictions

### Device platform restrictions

Define whether Windows, macOS, iOS/iPadOS, Android Enterprise, and personal devices may enrol.

### Device limit restrictions

Define how many devices each user may enrol. Use a limit that supports normal work patterns without enabling uncontrolled enrollment.

### Personally owned devices

Decide whether personal devices are:

- Blocked
- Allowed with MDM
- Allowed only with MAM/App Protection Policies
- Allowed only for selected pilot or exception groups

## Company Portal and Branding

Configure:

- Organization name and logo
- Support contact and helpdesk details
- Privacy statement
- Terms and conditions
- Device categories if required

## Validation Checklist

- [ ] Intune licence assigned to pilot users
- [ ] MDM authority confirmed
- [ ] MDM user scope configured
- [ ] Pilot groups created
- [ ] Platform restrictions reviewed
- [ ] Personal device strategy documented
- [ ] Device enrollment limits defined
- [ ] Company Portal support details configured
- [ ] One pilot enrollment completed successfully

> [!TIP]
> Start with the smallest practical pilot group. Enrollment mistakes can affect device ownership, policy targeting, access, and the user's ability to work.

---

[⬅ Previous](04-identity-authentication-hybrid.md) · [🏠 Home](../README.md) · [Next ➡](06-device-enrollment-methods.md)

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
