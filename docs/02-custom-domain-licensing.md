<a id="top"></a>

<!-- HANDBOOK-HEADER:START -->
<div align="center">

<img src="../assets/images/02-domain-licensing.svg" alt="🌐 Custom Domain & License Assignment" width="100%" />

[![Microsoft Intune](https://img.shields.io/badge/Microsoft-Intune-0078D4?logo=microsoft&logoColor=white)](https://learn.microsoft.com/mem/intune/)
[![Microsoft Entra ID](https://img.shields.io/badge/Microsoft-Entra_ID-5C2D91?logo=microsoftazure&logoColor=white)](https://learn.microsoft.com/entra/identity/)
[![Microsoft 365](https://img.shields.io/badge/Microsoft-365-D83B01?logo=microsoftoffice&logoColor=white)](https://learn.microsoft.com/microsoft-365/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](../README.md)

[🏠 Handbook Home](../README.md) · [🧪 Labs](../labs/README.md) · [⚡ Scripts](../scripts/README.md) · [📋 Templates](../templates/README.md)

</div>
<!-- HANDBOOK-HEADER:END -->

# 🌐 Custom Domain & License Assignment

[⬅ Previous](01-fundamentals-tenant-prerequisites.md) · [🏠 Home](../README.md) · [Next ➡](03-users-groups-guests-rbac.md)

---

## Why Add a Custom Domain?

A custom domain gives users a professional sign-in identity such as `user@companyname.com`, improves identity consistency, and supports branded Microsoft 365 services.

## Add and Verify a Domain

1. Open **Microsoft 365 Admin Center**.
2. Go to **Settings → Domains → Add domain**.
3. Enter the domain name.
4. Copy the TXT verification record.
5. Add the record at the DNS hosting provider.
6. Return to Microsoft 365 and select **Verify**.
7. Add required DNS records for Exchange, Teams, and other services.
8. Set the domain as default when ready.
9. Update user UPNs in a controlled change window.

### Typical DNS records

| Record | Typical Purpose |
|---|---|
| TXT | Domain verification and SPF |
| MX | Email routing |
| CNAME | Service discovery |
| SRV | Teams or legacy service discovery |

> [!WARNING]
> Verify existing mail flow and DNS dependencies before changing MX or Autodiscover records.

## Licence Options

| Licence | Typical Coverage |
|---|---|
| Intune Plan 1 | MDM, MAM, compliance, app management |
| Microsoft 365 Business Premium | Office apps, Exchange, Teams, Entra ID P1, Intune |
| Microsoft 365 E3/E5 | Enterprise productivity, compliance, security, management |
| Entra ID P1/P2 | Conditional Access, SSPR, Identity Protection, PIM depending on plan |
| EMS E3/E5 | Identity, device management, and security suite |

## Assign a Licence to a User

1. Open **Microsoft 365 Admin Center**.
2. Go to **Users → Active users**.
3. Select the user.
4. Open **Licences and apps**.
5. Confirm the user's usage location.
6. Select the required licence.
7. Save changes.

## Group-Based Licensing

Recommended process:

1. Create a dedicated security group.
2. Add pilot users.
3. Open **Entra Admin Center → Billing → Licences**.
4. Select the product licence.
5. Choose **Licensed groups → Assign**.
6. Review assignment errors after propagation.

## Best Practices

- Use groups instead of direct licence assignment where possible.
- Create separate groups for pilot and production users.
- Document service plans disabled within a licence.
- Review licence consumption monthly.
- Never remove the original `onmicrosoft.com` domain; it remains part of the tenant.

## Validation Checklist

- [ ] Domain status is Healthy
- [ ] TXT verification completed
- [ ] Required DNS records validated
- [ ] Pilot user can sign in using new UPN
- [ ] Usage location configured
- [ ] Intune service plan enabled
- [ ] Group-based licensing errors reviewed

---

[⬅ Previous](01-fundamentals-tenant-prerequisites.md) · [🏠 Home](../README.md) · [Next ➡](03-users-groups-guests-rbac.md)

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
