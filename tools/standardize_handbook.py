from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HEADER_START = '<!-- HANDBOOK-HEADER:START -->'
HEADER_END = '<!-- HANDBOOK-HEADER:END -->'
FOOTER_START = '<!-- HANDBOOK-FOOTER:START -->'
FOOTER_END = '<!-- HANDBOOK-FOOTER:END -->'

DOC_IMAGES = {
    '01-fundamentals-tenant-prerequisites.md': '01-fundamentals.svg',
    '02-custom-domain-licensing.md': '02-domain-licensing.svg',
    '03-users-groups-guests-rbac.md': '03-users-groups-rbac.svg',
    '04-identity-authentication-hybrid.md': '04-identity-authentication.svg',
    '05-intune-activation-enrollment.md': '05-intune-activation-enrollment.svg',
    '06-device-enrollment-methods.md': '06-device-enrollment.svg',
    '07-compliance-configuration-security.md': '07-compliance-security.svg',
    '08-apps-updates-reporting.md': '08-apps-updates-reporting.svg',
    '09-final-readiness-checklist.md': '09-readiness-checklist.svg',
    '10-windows-autopilot.md': '10-windows-autopilot.svg',
    '11-win32-app-packaging.md': '11-win32-app-packaging.svg',
    '12-troubleshooting-playbook.md': '12-troubleshooting-playbook.svg',
}

TARGETS = [(ROOT / 'docs' / name, image) for name, image in DOC_IMAGES.items()]
TARGETS += [
    (ROOT / 'labs' / 'README.md', '00-handbook-cover.svg'),
    (ROOT / 'scripts' / 'README.md', '00-handbook-cover.svg'),
    (ROOT / 'templates' / 'README.md', '00-handbook-cover.svg'),
]


def title_from(text: str, fallback: str) -> str:
    match = re.search(r'^#\s+(.+)$', text, flags=re.MULTILINE)
    return match.group(1).strip() if match else fallback


def strip_managed(text: str) -> str:
    text = re.sub(re.escape(HEADER_START) + r'.*?' + re.escape(HEADER_END) + r'\s*', '', text, flags=re.S)
    text = re.sub(re.escape(FOOTER_START) + r'.*?' + re.escape(FOOTER_END) + r'\s*', '', text, flags=re.S)
    text = re.sub(r'^<a id="top"></a>\s*', '', text)
    return text.strip()


def header(title: str, image: str) -> str:
    return f'''<a id="top"></a>

{HEADER_START}
<div align="center">

<img src="../assets/images/{image}" alt="{title}" width="100%" />

[![Microsoft Intune](https://img.shields.io/badge/Microsoft-Intune-0078D4?logo=microsoft&logoColor=white)](https://learn.microsoft.com/mem/intune/)
[![Microsoft Entra ID](https://img.shields.io/badge/Microsoft-Entra_ID-5C2D91?logo=microsoftazure&logoColor=white)](https://learn.microsoft.com/entra/identity/)
[![Microsoft 365](https://img.shields.io/badge/Microsoft-365-D83B01?logo=microsoftoffice&logoColor=white)](https://learn.microsoft.com/microsoft-365/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](../README.md)

[🏠 Handbook Home](../README.md) · [🧪 Labs](../labs/README.md) · [⚡ Scripts](../scripts/README.md) · [📋 Templates](../templates/README.md)

</div>
{HEADER_END}
'''


def footer() -> str:
    return f'''
{FOOTER_START}
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
{FOOTER_END}
'''


for path, image in TARGETS:
    if not path.exists():
        continue
    original = path.read_text(encoding='utf-8')
    title = title_from(original, path.stem.replace('-', ' ').title())
    body = strip_managed(original)
    path.write_text(header(title, image) + '\n' + body + '\n' + footer(), encoding='utf-8')
    print(f'Updated {path.relative_to(ROOT)}')
