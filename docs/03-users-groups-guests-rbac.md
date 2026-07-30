<a id="top"></a>

<!-- HANDBOOK-HEADER:START -->
<div align="center">

<img src="../assets/images/03-users-groups-rbac.svg" alt="👥 Users, Groups, Guests, RBAC & Roles" width="100%" />

[![Microsoft Intune](https://img.shields.io/badge/Microsoft-Intune-0078D4?logo=microsoft&logoColor=white)](https://learn.microsoft.com/mem/intune/)
[![Microsoft Entra ID](https://img.shields.io/badge/Microsoft-Entra_ID-5C2D91?logo=microsoftazure&logoColor=white)](https://learn.microsoft.com/entra/identity/)
[![Microsoft 365](https://img.shields.io/badge/Microsoft-365-D83B01?logo=microsoftoffice&logoColor=white)](https://learn.microsoft.com/microsoft-365/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](../README.md)

[🏠 Handbook Home](../README.md) · [🧪 Labs](../labs/README.md) · [⚡ Scripts](../scripts/README.md) · [📋 Templates](../templates/README.md)

</div>
<!-- HANDBOOK-HEADER:END -->

# 👥 Users, Groups, Guests, RBAC & Roles

[⬅ Previous](02-custom-domain-licensing.md) · [🏠 Home](../README.md) · [Next ➡](04-identity-authentication-hybrid.md)

---

## Create a Cloud User

**Portal path:** `Entra Admin Center → Identity → Users → All users → New user`

Configure:

- Display name
- User principal name
- Usage location
- Temporary password
- Group membership
- Licence assignment
- Manager and contact details

## Guest Users

Use guest accounts for controlled external collaboration.

Recommended flow:

1. Invite the external identity.
2. Require invitation redemption.
3. Add the guest to only the required groups.
4. Apply Conditional Access.
5. Perform regular access reviews.
6. Remove or disable stale guests.

## Group Types

| Group Type | Membership | Common Use |
|---|---|---|
| Security group | Assigned or dynamic | Access, licensing, Intune assignments |
| Microsoft 365 group | Assigned or dynamic users | Teams, SharePoint, Outlook collaboration |
| Assigned device group | Manual | Static pilot or application targeting |
| Dynamic user group | Rule-based | User department, licence, or attribute targeting |
| Dynamic device group | Rule-based | OS, ownership, model, or enrollment profile targeting |

## Suggested Intune Groups

```text
GRP-Intune-Licensed-Users
GRP-Intune-Pilot-Users
GRP-Intune-Windows-Devices
GRP-Intune-Corporate-Devices
GRP-Intune-BYOD-Devices
GRP-Intune-App-Deployment
GRP-Update-Ring-Pilot
GRP-Compliance-Pilot
```

## Dynamic Rule Examples

### Windows devices

```text
(device.deviceOSType -eq "Windows")
```

### Corporate-owned devices

```text
(device.deviceOwnership -eq "Company")
```

### Users by department

```text
(user.department -eq "Finance")
```

> [!NOTE]
> Validate dynamic membership before using a group for destructive settings, mandatory apps, or Conditional Access.

## RBAC Principles

- Apply least privilege.
- Separate normal user and admin accounts.
- Assign roles to groups rather than individuals where possible.
- Use Privileged Identity Management for eligible, time-bound access when available.
- Use Intune scope tags to restrict visibility and administration.
- Review privileged role assignments regularly.

## Common Roles

| Role | Purpose |
|---|---|
| Global Administrator | Full tenant control; emergency and limited use only |
| Intune Administrator | Manage devices, apps, policies, and enrollment |
| User Administrator | Manage user properties and lifecycle |
| Groups Administrator | Manage groups and memberships |
| Security Administrator | Manage security settings and investigations |
| Helpdesk Administrator | Reset passwords and perform limited support actions |
| Conditional Access Administrator | Create and manage Conditional Access policies |

## Validation Checklist

- [ ] Pilot user created
- [ ] Admin accounts separated from daily accounts
- [ ] Pilot groups created
- [ ] Dynamic rules validated
- [ ] Role assignments documented
- [ ] Guest access restrictions reviewed
- [ ] Emergency accounts excluded only where formally approved

---

[⬅ Previous](02-custom-domain-licensing.md) · [🏠 Home](../README.md) · [Next ➡](04-identity-authentication-hybrid.md)

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
