#!/usr/bin/env python3
"""Match officials against open policies with active/upcoming application windows.

Reads policy_contacts.csv and creates a "who to contact" matrix for incentives
with application windows currently open or opening soon.

Usage:
    python3 scripts/policy_contact_matcher.py [--active-only] [--days-ahead 30]

Options:
    --active-only    Show only policies with currently active application windows
    --days-ahead N   Include policies opening within N days (default: 30)
"""
from __future__ import annotations

import csv
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
POLICY_CONTACTS_FILE = DATA_DIR / "policy_contacts.csv"
POLICY_WINDOWS_FILE = DATA_DIR / "policy_windows.csv"
POLICY_EOI_CONTACTS_FILE = DATA_DIR / "policy_eoi_contacts.csv"

CSV_ENCODING = "utf-8-sig"
DATE_FORMAT = "%Y-%m-%d"
DEFAULT_DAYS_AHEAD = 30
TOP_CONTACTS = 3
RULE = "=" * 100
UNKNOWN_RANK = 99
# Rank order: Minister > Secretary > Minister of State > others.  Dict order matters:
# the first title found as a substring of the designation wins.
SENIORITY_RANK = {
    "minister": 1,
    "secretary": 2,
    "minister of state": 3,
    "additional secretary": 4,
    "joint secretary": 5,
    "director": 6,
}

Contact = Dict[str, str]
Windows = Dict[str, Tuple[datetime, datetime]]


def _read_rows(path: Path) -> List[Contact]:
    """Return all rows of a UTF-8(-BOM) CSV as dicts; [] when the file is absent."""
    if not path.exists():
        return []
    with path.open(encoding=CSV_ENCODING) as f:
        return list(csv.DictReader(f))


def load_policy_contacts() -> List[Contact]:
    """Load policy contacts from CSV."""
    if not POLICY_CONTACTS_FILE.exists():
        print(f"❌ File not found: {POLICY_CONTACTS_FILE}")
        return []
    return _read_rows(POLICY_CONTACTS_FILE)


def parse_windows(rows: List[Contact]) -> Windows:
    """Build {instrument: (start, end)} from policy_windows rows; bad dates are skipped."""
    windows: Windows = {}
    for row in rows:
        instrument = row.get('instrument', '').strip()
        start_str = row.get('application_start_date', '').strip()
        end_str = row.get('application_end_date', '').strip()
        if instrument and start_str and end_str:
            try:
                windows[instrument] = (datetime.strptime(start_str, DATE_FORMAT),
                                       datetime.strptime(end_str, DATE_FORMAT))
            except ValueError:
                pass
    return windows


def load_policy_windows() -> Windows:
    """Load application window dates from CSV.

    Returns: {instrument: (start_date, end_date), ...}
    """
    return parse_windows(_read_rows(POLICY_WINDOWS_FILE))


def load_eoi_contacts() -> List[Contact]:
    """Load EOI and press-release contacts from CSV.

    These supplement the main policy_contacts.csv with additional officials
    mentioned in Expression of Interest documents and official notifications.
    """
    return _read_rows(POLICY_EOI_CONTACTS_FILE)


def get_window_status(start: datetime, end: datetime, today: Optional[datetime] = None) -> Tuple[str, int]:
    """Get status and days remaining/until opening.

    Returns: (status_string, days_count)
    - If active: ("ACTIVE", days_remaining)
    - If opening soon: ("OPENING_SOON", days_until_open)
    - If closed: ("CLOSED", days_since_close)
    """
    if today is None:
        today = datetime.now()

    if today < start:
        days = (start - today).days
        return ("OPENING_SOON", days)
    elif today <= end:
        days = (end - today).days
        return ("ACTIVE", days)
    else:
        days = (today - end).days
        return ("CLOSED", days)


def filter_by_active_windows(contacts: List[Contact], windows: Windows,
                             active_only: bool = True, days_ahead: int = DEFAULT_DAYS_AHEAD,
                             today: Optional[datetime] = None) -> List[Contact]:
    """Filter contacts to only include policies with active/upcoming application windows.

    Args:
        contacts: List of policy contacts
        windows: Dict of {instrument: (start_date, end_date)}
        active_only: If True, only show ACTIVE windows. If False, include OPENING_SOON
        days_ahead: Include policies opening within N days
        today: Reference date (defaults to now; injectable for tests)

    Returns: Filtered contact list with window_status added
    """
    if today is None:
        today = datetime.now()
    filtered = []

    for contact in contacts:
        instrument = contact.get('instrument', '').strip()
        if not instrument:
            continue

        if instrument not in windows:
            # No window data for this policy; skip in active-only mode
            if not active_only:
                contact_copy = contact.copy()
                contact_copy['window_status'] = 'NO_DATA'
                contact_copy['days_info'] = 'N/A'
                filtered.append(contact_copy)
            continue

        start, end = windows[instrument]
        status, days = get_window_status(start, end, today)

        if active_only and status != 'ACTIVE':
            continue

        if not active_only and status == 'OPENING_SOON' and days > days_ahead:
            continue

        if status == 'CLOSED':
            continue

        contact_copy = contact.copy()
        contact_copy['window_status'] = status
        contact_copy['days_info'] = str(days)
        filtered.append(contact_copy)

    return filtered


def group_by_policy(contacts: List[Contact]) -> Dict[str, List[Contact]]:
    """Group contacts by policy instrument."""
    grouped = defaultdict(list)
    for contact in contacts:
        instrument = contact.get('instrument', '').strip()
        if instrument:
            grouped[instrument].append(contact)
    return grouped


def get_open_policies(contacts: List[Contact]) -> List[str]:
    """Extract unique open policy instruments."""
    open_policies = set()
    for contact in contacts:
        status = contact.get('status', '').lower()
        instrument = contact.get('instrument', '').strip()
        if instrument and 'open' in status:
            open_policies.add(instrument)
    return sorted(open_policies)


def seniority_rank(contact: Contact) -> int:
    """Seniority rank of a contact's designation (1 = most senior, 99 = unknown)."""
    designation = contact.get('designation', '').lower()
    for title, rank in SENIORITY_RANK.items():
        if title in designation:
            return rank
    return UNKNOWN_RANK


def rank_contacts_by_seniority(contacts: List[Contact]) -> List[Contact]:
    """Rank contacts by designation seniority (stable for equal ranks)."""
    return sorted(contacts, key=seniority_rank)


def print_policy_contact_matrix(policies_by_instrument: Dict[str, List[Contact]]) -> None:
    """Print a matrix of policies and their top contacts."""
    print("\n" + RULE)
    print("🎯 OPEN POLICY INCENTIVES & TOP CONTACTS (WHO TO CONTACT)")
    print(RULE)

    for instrument, contacts in sorted(policies_by_instrument.items()):
        if not contacts:
            continue

        status = contacts[0].get('status', 'unknown')
        offering_entity = contacts[0].get('offering_entity', 'unknown')
        instrument_type = contacts[0].get('instrument_type', 'unknown')
        source_url = contacts[0].get('source_url', '')
        window_status = contacts[0].get('window_status', None)
        days_info = contacts[0].get('days_info', None)

        print(f"\n📋 {instrument.upper()}")
        print(f"   Sector: {offering_entity} | Type: {instrument_type}")
        print(f"   Status: {status}")

        # Application window status
        if window_status:
            if window_status == 'ACTIVE':
                print(f"   ⏰ APPLICATION WINDOW: OPEN ({days_info} days remaining)")
            elif window_status == 'OPENING_SOON':
                print(f"   ⏰ APPLICATION WINDOW: Opens in {days_info} days")
            elif window_status == 'NO_DATA':
                print("   ⏰ APPLICATION WINDOW: No data available")

        if source_url:
            print(f"   Website: {source_url}")

        # Rank and show top 3 contacts
        ranked = rank_contacts_by_seniority(contacts)
        print("\n   🤝 Top Contacts (by seniority):")

        for i, contact in enumerate(ranked[:TOP_CONTACTS], 1):
            name = contact.get('contact_name', '').strip()
            designation = contact.get('designation', '').strip()
            division = contact.get('division', '').strip()
            phones = contact.get('phones', '').strip()
            email = contact.get('email', '').strip()

            if not name:
                continue

            print(f"\n      {i}. {name}")
            if designation:
                print(f"         Role: {designation}")
            if division:
                print(f"         Division: {division}")
            if phones:
                phone_list = [p.strip() for p in phones.split(',')]
                print(f"         Phone: {', '.join(phone_list)}")
            if email:
                print(f"         Email: {email}")
            else:
                print("         Email: [Not available]")


def print_summary_by_sector(policies_by_instrument: Dict[str, List[Contact]]):
    """Print summary grouped by sector/entity."""
    print("\n" + RULE)
    print("📊 SUMMARY BY SECTOR")
    print(RULE)

    by_sector = defaultdict(list)
    for instrument, contacts in policies_by_instrument.items():
        if contacts:
            sector = contacts[0].get('offering_entity', 'Unknown').strip()
            by_sector[sector].append(instrument)

    for sector, instruments in sorted(by_sector.items()):
        print(f"\n{sector}")
        for instrument in instruments:
            print(f"  • {instrument}")


def print_contact_lookup(policies_by_instrument: Dict[str, List[Contact]]):
    """Print quick lookup: who is contact for what."""
    print("\n" + RULE)
    print("📇 CONTACT LOOKUP (Who is responsible for what)")
    print(RULE)

    by_contact = defaultdict(list)
    for instrument, contacts in policies_by_instrument.items():
        for contact in contacts:
            name = contact.get('contact_name', '').strip()
            designation = contact.get('designation', '').strip()
            email = contact.get('email', '').strip()

            if name:
                key = (name, designation, email)
                by_contact[key].append(instrument)

    for (name, designation, email), instruments in sorted(by_contact.items()):
        if name:
            print(f"\n{name}")
            print(f"  Designation: {designation}")
            if email:
                print(f"  Email: {email}")
            print("  Policies:")
            for instrument in sorted(instruments):
                print(f"    • {instrument}")


def find_unassigned_policies(contacts: List[Contact]) -> List[Tuple[str, str]]:
    """Open policies with no named contact, as (instrument, instrument_type) pairs."""
    unassigned = []
    for policy in get_open_policies(contacts):
        matching = [c for c in contacts if c.get('instrument', '').strip() == policy]
        if not any(c.get('contact_name', '').strip() for c in matching):
            unassigned.append((policy, matching[0].get('instrument_type', '') if matching else ''))
    return unassigned


def print_missing_contacts(contacts: Optional[List[Contact]] = None) -> None:
    """Identify policies without contacts assigned (reloads the CSV when not given)."""
    print("\n" + RULE)
    print("⚠️  POLICIES WITHOUT ASSIGNED CONTACTS")
    print(RULE)

    if contacts is None:
        contacts = load_policy_contacts()
    no_contact_policies = find_unassigned_policies(contacts)

    if no_contact_policies:
        for policy, instr_type in no_contact_policies:
            print(f"\n• {policy}")
            if instr_type:
                print(f"  Type: {instr_type}")
    else:
        print("\n✅ All open policies have assigned contacts!")


def print_application_window_template():
    """Print template for adding application window data."""
    print("\n" + RULE)
    print("🔄 TO ADD APPLICATION WINDOW DATA")
    print(RULE)
    print("""
Application windows can be added by:

1. Web scraping policy websites (using Selenium or Playwright):
   - Extract "Application opens" and "Application closes" dates
   - Parse PDF notices with dateutil
   - Store in policy_windows.csv with columns:
     * instrument
     * application_start_date (YYYY-MM-DD)
     * application_end_date (YYYY-MM-DD)
     * last_updated (ISO timestamp)
     * source_url (where date was scraped)

2. Example: policy_windows.csv

   instrument,application_start_date,application_end_date,notification_url
   "Agriculture Infrastructure Fund (AIF)","2026-06-01","2026-12-31","agriinfra.dac.gov.in/notification"
   "MIDH","2026-01-01","2026-08-31","midh.gov.in"
   "PMFBY","2025-06-01","2026-05-31","pmfby.gov.in"

3. Then filter open policies by comparing today's date against these windows.

Current status: {0} open policy instruments identified.
""".format(len(get_open_policies(load_policy_contacts()))))


def parse_args(argv: List[str]) -> Tuple[bool, int]:
    """Return (active_only, days_ahead) from argv; a malformed --days-ahead is ignored."""
    active_only = '--active-only' in argv
    days_ahead = DEFAULT_DAYS_AHEAD
    for i, arg in enumerate(argv):
        if arg == '--days-ahead' and i + 1 < len(argv):
            try:
                days_ahead = int(argv[i + 1])
            except ValueError:
                pass
    return active_only, days_ahead


def main(argv: Optional[List[str]] = None) -> int:
    """Main entry point."""
    active_only, days_ahead = parse_args(sys.argv if argv is None else argv)

    # Load data
    contacts = load_policy_contacts()
    eoi_contacts = load_eoi_contacts()
    windows = load_policy_windows()

    if not contacts and not eoi_contacts:
        print("❌ No contacts loaded")
        return 1

    # Merge EOI contacts with main contacts
    if eoi_contacts:
        contacts.extend(eoi_contacts)

    # Filter by application windows if requested
    if active_only or windows:
        filtered_contacts = filter_by_active_windows(contacts, windows, active_only, days_ahead)
        print("✅ Filtering by application windows...")
        print(f"   • Total contacts (before filter): {len(contacts)}")
        print(f"   • Active window policies: {len(filtered_contacts)}")
        print(f"   • Window data available for {len(windows)} policies")
        contacts = filtered_contacts

    policies_by_instrument = group_by_policy(contacts)
    open_policies = get_open_policies(contacts)

    print("\n📈 Dataset Summary")
    print(f"   • Total contacts loaded: {len(contacts)}")
    print(f"   • Unique policies: {len(policies_by_instrument)}")
    print(f"   • Open policies: {len(open_policies)}")
    if active_only and windows:
        active_count = sum(1 for c in windows.values() if get_window_status(c[0], c[1])[0] == 'ACTIVE')
        print(f"   • Policies with ACTIVE application windows: {active_count}")

    # Print matrices and summaries
    print_policy_contact_matrix(policies_by_instrument)
    print_summary_by_sector(policies_by_instrument)
    print_contact_lookup(policies_by_instrument)
    print_missing_contacts()
    print_application_window_template()

    print("\n" + RULE)
    print("✅ Analysis complete")
    print(RULE)

    return 0


if __name__ == "__main__":
    sys.exit(main())
