from datetime import datetime
import json

def get_entries(entries):
    entries_data = {}

    entries = json.loads(entries)

    entry_days = sorted(
        set(
            map(lambda entry: datetime.strptime(entry['day_entry']['spent_at'], '%Y-%m-%d'), entries)
        )
    )
    entries_data['start_date'] = entry_days[0].strftime('%Y-%m-%d')
    entries_data['end_date'] = entry_days[-1].strftime('%Y-%m-%d')
    entries_data['entries'] = entries

    return entries_data


def get_project_by_id(projects, project_id):
    for p in projects:
        if project_id == p['project']['id']:
            return p
    return None

def get_project_name(projects, project_id):
    p = get_project_by_id(projects, project_id)
    return p['project']['name'] \
        if p and 'project' in p and 'name' in p['project'] \
        else None

def get_project_client(projects, project_id):
    p = get_project_by_id(projects, project_id)
    return p['project']['client_id'] \
        if p and 'project' in p and 'client_id' in p['project'] \
        else None
