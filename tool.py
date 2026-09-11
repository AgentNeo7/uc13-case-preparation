"""Standalone deterministic synthetic prototype. No runtime integration or domain authority."""
import argparse
import copy
import datetime
import hashlib
import json
import math
from pathlib import Path
import sys


def obj(x, keys):
    if not isinstance(x, dict) or set(x) != set(keys.split()):
        raise ValueError("object fields must be: " + keys)
    return x


def text(x):
    if not isinstance(x, str) or not x or len(x) > 2048:
        raise ValueError("expected nonempty bounded string")
    return x


def arr(x):
    if not isinstance(x, list) or len(x) > 500:
        raise ValueError("expected list of at most 500 elements")
    return x


def names(x):
    values = [text(v) for v in arr(x)]
    if len(values) != len(set(values)):
        raise ValueError("duplicate identifiers")
    return values


def num(x, minimum=0):
    if type(x) not in (int, float) or not math.isfinite(x) or x < minimum or x > 1e12:
        raise ValueError("invalid bounded number")
    return x


def integer(x, minimum=0):
    if type(x) is not int:
        raise ValueError("expected integer")
    return num(x, minimum)


def boolean(x):
    if type(x) is not bool:
        raise ValueError("expected boolean")
    return x


def unique(rows):
    ids = [text(x["id"]) for x in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate record ID")


def scalar(x):
    if x is not None and type(x) not in (str, int, float, bool):
        raise ValueError("expected scalar value")
    if type(x) in (int,float) and not math.isfinite(x):
        raise ValueError("nonfinite number")
    return x


def result(**kw):
    return {"evidence_class": "simulated", "analysis_completed": True, **kw}


def analyze(payload):
    obj(payload, "spec_version evidence_class data")
    if type(payload["spec_version"]) is not int or payload["spec_version"] != 1 or payload["evidence_class"] != "simulated":
        raise ValueError("only spec_version 1 synthetic evidence_class simulated supported")
    return run(copy.deepcopy(payload["data"]))


def matches(actual, expected):
    if isinstance(expected, dict):
        return isinstance(actual, dict) and all(k in actual and matches(actual[k], v) for k,v in expected.items())
    return actual == expected


def read_json(path):
    if path.stat().st_size > 1000000:
        raise ValueError("input exceeds 1000000 bytes")
    return json.loads(path.read_text())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    p.add_argument("--expect", type=Path, help="optional recursive subset oracle; mismatch exits 1")
    a=p.parse_args()
    try:
        if a.input.resolve() == a.output.resolve() or (a.expect and a.expect.resolve() == a.output.resolve()):
            raise ValueError("output must not overwrite input or oracle")
        output=analyze(read_json(a.input))
        expected=read_json(a.expect) if a.expect else None
        a.output.write_text(json.dumps(output,indent=2,sort_keys=True,allow_nan=False)+"\n")
        return 0 if expected is None or matches(output,expected) else 1
    except (ValueError, KeyError, TypeError, OSError, RecursionError, OverflowError) as e:
        print("invalid input: "+str(e),file=sys.stderr)
        return 2

def run(d):
    obj(d,'entity as_of requirements facts');text(d['entity']);asof=datetime.date.fromisoformat(d['as_of'])
    requirements=arr(d['requirements']);facts=arr(d['facts']);unique(facts)
    if not requirements:raise ValueError('nonempty explicit checklist required')
    fields=[]
    for r in requirements:
        obj(r,'field max_age_days authorities');fields.append(text(r['field']));integer(r['max_age_days']);names(r['authorities'])
    if len(set(fields))!=len(fields):raise ValueError('duplicate requirement')
    for f in facts:
        obj(f,'id entity field value date authority source supersedes')
        for k in ['entity','field','authority','source']:text(f[k])
        scalar(f['value']);datetime.date.fromisoformat(f['date']);names(f['supersedes'])
        if f['id'] in f['supersedes']:raise ValueError('self supersession')
    ids={f['id']:f for f in facts}
    for f in facts:
        for prev in f['supersedes']:
            if prev not in ids or any(ids[prev][k]!=f[k] for k in ['entity','field','authority']) or ids[prev]['date']>=f['date']:
                raise ValueError('invalid supersession chain')
    relevant=[f for f in facts if f['entity']==d['entity'] and f['date']<=d['as_of']]
    superseded={x for f in relevant for x in f['supersedes']}
    established=[];missing=[];conflicts=[];stale=[];unauthorized=[];unknown_values=[]
    for r in requirements:
        fs=[]
        for f in relevant:
            if f['field']!=r['field'] or f['id'] in superseded:continue
            if f['value'] is None:unknown_values.append(f['id']);continue
            if f['authority'] not in r['authorities']:unauthorized.append(f['id']);continue
            if (asof-datetime.date.fromisoformat(f['date'])).days>r['max_age_days']:stale.append(f['id']);continue
            fs.append(f)
        if not fs:missing.append(r['field'])
        elif len({json.dumps(f['value'],sort_keys=True) for f in fs})>1:conflicts.append(r['field'])
        else:established.append({'field':r['field'],'value':fs[0]['value'],'evidence_ids':sorted(f['id'] for f in fs)})
    return result(status='incomplete' if missing or conflicts else 'complete_within_declared_checklist', established=established,missing=sorted(missing),conflicts=sorted(conflicts),stale_evidence_ids=sorted(stale),unknown_value_ids=sorted(unknown_values),unapproved_authority_ids=sorted(unauthorized),superseded_ids=sorted(superseded),excluded_entity_ids=sorted(f['id'] for f in facts if f['entity']!=d['entity']),sources={f['id']:f['source'] for f in facts})

if __name__ == "__main__":
    sys.exit(main())
