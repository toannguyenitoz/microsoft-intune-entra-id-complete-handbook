<a id="top"></a>

<!-- HANDBOOK-HEADER:START -->
<div align="center">

<img src="../assets/images/01-fundamentals.svg" alt="🏢 Fundamentals, Tenant & Prerequisites" width="100%" />

[![Microsoft Intune](https://img.shields.io/badge/Microsoft-Intune-0078D4?logo=microsoft&logoColor=white)](https://learn.microsoft.com/mem/intune/)
[![Microsoft Entra ID](https://img.shields.io/badge/Microsoft-Entra_ID-5C2D91?logo=microsoftazure&logoColor=white)](https://learn.microsoft.com/entra/identity/)
[![Microsoft 365](https://img.shields.io/badge/Microsoft-365-D83B01?logo=microsoftoffice&logoColor=white)](https://learn.microsoft.com/microsoft-365/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](../README.md)

[🏠 Handbook Home](../README.md) · [🧪 Labs](../labs/README.md) · [⚡ Scripts](../scripts/README.md) · [📋 Templates](../templates/README.md)

</div>
<!-- HANDBOOK-HEADER:END -->

# 🏢 Fundamentals, Tenant & Prerequisites

[🏠 Home](../README.md) · [Next ➡](02-custom-domain-licensing.md)

---

## 1. What Is Microsoft Intune?

Microsoft Intune is a cloud-based endpoint management service used to manage and secure devices, applications, and organizational data.

### Core capabilities

- Mobile Device Management (MDM)
- Mobile Application Management (MAM)
- Device configuration and compliance
- Application deployment
- Endpoint security
- Windows update management
- Reporting and remote actions
- Integration with Microsoft Entra ID and Microsoft Defender

## 2. What Is Microsoft Entra ID?

Microsoft Entra ID is Microsoft's cloud identity and access management platform.

It manages:

- Users, groups, guests, and devices
- Authentication and authorization
- Single Sign-On
- Multi-Factor Authentication
- Conditional Access
- Privileged roles
- Enterprise applications and service principals

## 3. Required Admin Portals

| Portal | Use |
|---|---|
| Microsoft 365 Admin Center | Users, licences, domains, service health |
| Microsoft Entra Admin Center | Identity, roles, authentication, Conditional Access |
| Microsoft Intune Admin Center | Devices, apps, policies, enrollment, reports |
| Microsoft Defender Portal | Endpoint security and incidents |

## 4. Prerequisites Checklist

- [ ] Microsoft 365 or Intune tenant exists
- [ ] Global Administrator account available
- [ ] Separate Intune Administrator account created
- [ ] Supported licence assigned
- [ ] Business or organizational usage location configured
- [ ] Pilot users created
- [ ] Test device available
- [ ] Reliable internet connection available
- [ ] Custom domain planned or already owned
- [ ] Emergency access accounts documented

## 5. Recommended Setup Sequence

```text
Create tenant
→ Add custom domain
→ Purchase and assign licences
→ Create users and groups
→ Configure admin roles
→ Configure MFA and SSPR
→ Activate Intune enrollment
→ Configure restrictions
→ Enrol pilot devices
→ Apply configuration and compliance
→ Deploy apps and updates
→ Monitor and improve
```

## 6. Key Terms

| Term | Meaning |
|---|---|
| Tenant | Dedicated Microsoft cloud environment for an organization |
| UPN | User sign-in name, usually user@company.com |
| MDM | Device-level management |
| MAM | App-level data protection and management |
| Company Portal | User-facing app for enrollment, apps, and support |
| Autopilot | Cloud-driven Windows provisioning |
| Conditional Access | Policy engine controlling access based on conditions |

## 7. Initial Lab

1. Sign in to the Microsoft 365 Admin Center.
2. Confirm the tenant name and default `onmicrosoft.com` domain.
3. Open Microsoft Entra Admin Center and locate the tenant ID.
4. Open Intune Admin Center and confirm the service is accessible.
5. Create one standard pilot user and one pilot security group.
6. Record the environment in a change log.

> [!TIP]
> Use a naming standard from day one. Consistent group, policy, app, and profile names make troubleshooting significantly easier.

---

[🏠 Home](../README.md) · [Next: Custom Domain & Licensing ➡](02-custom-domain-licensing.md)

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
