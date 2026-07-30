<div align="center">

# ☁️ Microsoft Intune & Entra ID Complete Setup Handbook

### A practical, lab-driven guide for building, securing, managing, and troubleshooting a modern Microsoft cloud environment

[![Microsoft Intune](https://img.shields.io/badge/Microsoft-Intune-0078D4?logo=microsoft&logoColor=white)](https://learn.microsoft.com/mem/intune/)
[![Microsoft Entra ID](https://img.shields.io/badge/Microsoft-Entra_ID-5C2D91?logo=microsoftazure&logoColor=white)](https://learn.microsoft.com/entra/identity/)
[![Microsoft 365](https://img.shields.io/badge/Microsoft-365-D83B01?logo=microsoftoffice&logoColor=white)](https://learn.microsoft.com/microsoft-365/)
[![Windows 11](https://img.shields.io/badge/Windows-11-0078D6?logo=windows11&logoColor=white)](https://www.microsoft.com/windows/)
[![PowerShell](https://img.shields.io/badge/PowerShell-Automation-5391FE?logo=powershell&logoColor=white)](https://learn.microsoft.com/powershell/)
[![Documentation](https://img.shields.io/badge/Type-Hands--on%20Handbook-success)](#-learning-path)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](#-roadmap)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Plan → Configure → Enrol → Secure → Deploy → Monitor → Troubleshoot → Improve**

</div>

---

## 📘 About This Repository

This repository is a complete Microsoft Intune and Microsoft Entra ID learning handbook designed for:

- IT Support and Service Desk technicians
- Endpoint and Modern Workplace administrators
- Microsoft 365 administrators
- System administrators moving from on-premises AD to cloud management
- Students preparing for practical labs, interviews, or Microsoft certification paths

The content follows a logical tenant-to-production sequence and includes portal paths, implementation checklists, PowerShell examples, lab exercises, troubleshooting workflows, and production-readiness guidance.

> [!IMPORTANT]
> Test all policies in a dedicated pilot group before broad production deployment. Conditional Access, compliance, enrollment restrictions, and application assignments can lock out users or disrupt business operations when configured incorrectly.

---

## 🧭 Learning Path

| Phase | Topic | Outcome |
|---|---|---|
| 1 | Fundamentals and tenant prerequisites | Understand services, portals, licensing, and setup order |
| 2 | Domains, identities, users, groups, and roles | Build the identity foundation |
| 3 | Authentication and hybrid identity | Configure MFA, SSPR, Entra Join, PHS, SSO, and Entra Connect |
| 4 | Intune activation and enrollment | Enable MDM and enrol corporate or BYOD devices |
| 5 | Configuration, compliance, and security | Apply settings, compliance, Conditional Access, and endpoint protection |
| 6 | Applications, scripts, and updates | Deploy apps, Win32 packages, remediation scripts, and Windows updates |
| 7 | Reporting and troubleshooting | Investigate failed deployments, enrollment issues, and policy conflicts |
| 8 | Production readiness | Validate the environment before go-live |

---

## 📚 Table of Contents

### Core Handbook

1. [🏢 Fundamentals, Tenant & Prerequisites](docs/01-fundamentals-tenant-prerequisites.md)
2. [🌐 Custom Domain & License Assignment](docs/02-custom-domain-licensing.md)
3. [👥 Users, Groups, Guests, RBAC & Roles](docs/03-users-groups-guests-rbac.md)
4. [🔐 MFA, SSPR, Join, Connect, PHS, SSO & ADFS](docs/04-identity-authentication-hybrid.md)
5. [⚙️ Intune Activation, Auto Enrollment & Restrictions](docs/05-intune-activation-enrollment.md)
6. [💻 Device Enrollment Methods](docs/06-device-enrollment-methods.md)
7. [🛡️ Compliance, Configuration, Conditional Access & Endpoint Security](docs/07-compliance-configuration-security.md)
8. [📦 Apps, Updates, Reporting & Troubleshooting](docs/08-apps-updates-reporting.md)
9. [✅ Final Production Readiness Checklist](docs/09-final-readiness-checklist.md)

### Extended Practical Modules

- [🚀 Windows Autopilot Deployment](docs/10-windows-autopilot.md)
- [📦 Win32 Application Packaging](docs/11-win32-app-packaging.md)
- [🧰 Troubleshooting Playbook](docs/12-troubleshooting-playbook.md)
- [🧪 Hands-on Lab Scenarios](labs/README.md)
- [⚡ PowerShell Scripts](scripts/README.md)
- [📋 Reusable Templates](templates/README.md)

---

## 🏗️ Recommended Setup Flow

```text
Tenant
  ↓
Custom Domain
  ↓
Licensing
  ↓
Users and Groups
  ↓
RBAC and Administrative Roles
  ↓
MFA and SSPR
  ↓
Intune Activation
  ↓
Enrollment Configuration
  ↓
Device Enrollment
  ↓
Configuration Profiles
  ↓
Compliance Policies
  ↓
Conditional Access
  ↓
Endpoint Security
  ↓
Applications and Updates
  ↓
Reporting and Troubleshooting
```

---

## 🧰 Required Admin Portals

| Portal | Primary Purpose |
|---|---|
| Microsoft 365 Admin Center | Tenant, users, licences, domains, service health |
| Microsoft Entra Admin Center | Identity, authentication, roles, groups, Conditional Access |
| Microsoft Intune Admin Center | Devices, apps, policies, enrollment, reports |
| Microsoft Defender Portal | Endpoint security, incidents, vulnerabilities, security posture |
| Microsoft Purview Portal | Compliance, information protection, audit, retention |

---

## 🧪 Lab Environment Recommendation

```text
1 x Microsoft 365 Developer or trial tenant
1 x Global Administrator emergency account
1 x Intune Administrator account
1 x Standard test user
1 x Pilot user group
1 x Windows 11 virtual machine
1 x Android or iOS test device
Optional: Windows Server domain controller for hybrid labs
```

### Suggested Test Groups

```text
GRP-Intune-Licensed-Users
GRP-Intune-Pilot-Users
GRP-Intune-Windows-Devices
GRP-Intune-App-Deployment
GRP-Update-Ring-Pilot
GRP-Compliance-Pilot
GRP-Conditional-Access-Pilot
```

---

## 🔐 Security Principles Used Throughout This Handbook

- Apply least privilege
- Separate daily admin and emergency access accounts
- Use pilot groups before production rollout
- Require MFA for administrators
- Maintain at least two emergency access accounts
- Use device compliance with Conditional Access
- Prefer cloud-native management where practical
- Document every production policy and assignment
- Monitor sign-in logs, audit logs, deployment reports, and service health

---

## 📂 Repository Structure

```text
microsoft-intune-entra-id-complete-handbook/
├── README.md
├── LICENSE
├── docs/
│   ├── 01-fundamentals-tenant-prerequisites.md
│   ├── 02-custom-domain-licensing.md
│   ├── 03-users-groups-guests-rbac.md
│   ├── 04-identity-authentication-hybrid.md
│   ├── 05-intune-activation-enrollment.md
│   ├── 06-device-enrollment-methods.md
│   ├── 07-compliance-configuration-security.md
│   ├── 08-apps-updates-reporting.md
│   ├── 09-final-readiness-checklist.md
│   ├── 10-windows-autopilot.md
│   ├── 11-win32-app-packaging.md
│   └── 12-troubleshooting-playbook.md
├── labs/
│   └── README.md
├── scripts/
│   ├── README.md
│   ├── Get-IntuneDeviceDiagnostics.ps1
│   └── Test-IntunePrerequisites.ps1
└── templates/
    ├── README.md
    ├── application-deployment-checklist.md
    ├── conditional-access-change-record.md
    └── policy-design-template.md
```

---

## 🎯 Key Outcomes

After completing the handbook, you should be able to:

- Configure a Microsoft 365 and Intune tenant foundation
- Add and validate a custom domain
- Create users, groups, guests, dynamic groups, and role assignments
- Configure MFA, SSPR, authentication methods, and hybrid identity basics
- Enable automatic enrollment and enrollment restrictions
- Enrol Windows, Android, iOS/iPadOS, and macOS devices
- Create configuration, compliance, Conditional Access, and endpoint security policies
- Package and deploy Microsoft 365, Store, and Win32 applications
- Configure update rings, feature updates, and quality updates
- Read Intune logs and troubleshoot common deployment failures
- Validate a tenant using a production-readiness checklist

---

## 🗺️ Roadmap

- [x] Core nine-part setup handbook
- [x] Windows Autopilot module
- [x] Win32 application packaging module
- [x] Troubleshooting playbook
- [x] PowerShell diagnostics starter scripts
- [x] Reusable operational templates
- [ ] Android Enterprise advanced scenarios
- [ ] Apple Automated Device Enrollment
- [ ] Microsoft Graph automation examples
- [ ] Endpoint Privilege Management
- [ ] Windows 365 and Cloud PC integration
- [ ] Intune Suite advanced capabilities

---

## 🤝 Contributions

Contributions, lab screenshots, corrections, and real-world troubleshooting cases are welcome. Please open an issue or submit a pull request with a clear description of the proposed change.

---

## 👨‍💻 Author

**Xuan Toan Nguyen**  
IT Support · Systems Administration · Microsoft 365 · Azure · Modern Workplace  
📍 Adelaide, South Australia  
🏅 Silver Medalist — WorldSkills Australia SA Regional Competition 2026, Cloud Computing

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Toan%20Nguyen-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/toan-nguyen-it-oz)
[![GitHub](https://img.shields.io/badge/GitHub-toannguyenitoz-181717?logo=github&logoColor=white)](https://github.com/toannguyenitoz)

---

<div align="center">

### ⭐ Support the Project

If this handbook is useful, please consider giving the repository a star and sharing it with other IT professionals.

**#MicrosoftIntune · #MicrosoftEntraID · #Microsoft365 · #ModernWorkplace · #ToanNguyenITOz**

[⬆ Back to Top](#️-microsoft-intune--entra-id-complete-setup-handbook)

</div>
