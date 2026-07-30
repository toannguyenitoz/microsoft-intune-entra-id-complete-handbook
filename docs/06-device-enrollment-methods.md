# 💻 Device Enrollment Methods

[⬅ Previous](05-intune-activation-enrollment.md) · [🏠 Home](../README.md) · [Next ➡](07-compliance-configuration-security.md)

---

## Windows Enrollment Options

### Entra Join

1. Open **Settings → Accounts → Access work or school**.
2. Select **Connect**.
3. Choose **Join this device to Microsoft Entra ID**.
4. Sign in with a licensed work account.
5. Restart when prompted.
6. Confirm the device appears in Entra ID and Intune.

### Company Portal Enrollment

1. Install Company Portal.
2. Sign in using a work account.
3. Follow the enrollment wizard.
4. Allow device management.
5. Review compliance and required apps.

### Windows Autopilot

1. Collect the hardware hash.
2. Import or register the device.
3. Create an Autopilot deployment profile.
4. Assign the profile to a device group.
5. Configure Enrollment Status Page.
6. Reset or start the device in OOBE.
7. Validate automated provisioning.

## macOS Enrollment

- Configure Apple MDM push certificate.
- Configure Apple Business Manager integration when available.
- Deploy Company Portal.
- Enrol and approve the management profile.
- Deploy compliance, FileVault, certificates, and required apps.

## Android Enterprise Enrollment

Common models:

- Personally owned work profile
- Corporate-owned fully managed
- Corporate-owned work profile
- Dedicated device

Connect Managed Google Play, assign apps, define enrollment profiles, and validate work-profile separation.

## iPhone and iPad Enrollment

- Install Company Portal for user enrollment scenarios.
- Use Apple Automated Device Enrollment for corporate-owned devices.
- Configure Apple tokens and enrollment profiles.
- Confirm management profile installation.
- Apply compliance and app protection policies.

## BYOD vs Corporate-Owned

| Area | BYOD | Corporate-Owned |
|---|---|---|
| Ownership | User | Organization |
| Management | Limited or app-focused | Full device control |
| Personal data | Must remain private | Corporate use governed by policy |
| Wipe action | Prefer selective wipe | Full wipe may be appropriate |
| Typical use | Email and collaboration | Standard managed workforce |

## Post-Enrollment Verification

- [ ] Device exists in Entra ID
- [ ] Device exists in Intune
- [ ] Ownership is correct
- [ ] Primary user is correct
- [ ] Compliance evaluates successfully
- [ ] Configuration profiles apply
- [ ] Required apps install
- [ ] Company resources are accessible
- [ ] Support and recovery actions are documented

---

[⬅ Previous](05-intune-activation-enrollment.md) · [🏠 Home](../README.md) · [Next ➡](07-compliance-configuration-security.md)
