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
