# scripts/nmap_xml_to_csv.py
import sys, csv, xml.etree.ElementTree as ET
if len(sys.argv) < 2:
    print("usage: python3 scripts/nmap_xml_to_csv.py <input.xml> > output.csv", file=sys.stderr)
    sys.exit(1)
root = ET.parse(sys.argv[1]).getroot()
rows = []
for host in root.findall("host"):
    addr_el = host.find("address")
    addr = addr_el.attrib.get("addr", "") if addr_el is not None else ""
    for port in host.findall("./ports/port"):
        p = port.attrib["portid"]; proto = port.attrib["protocol"]
        state_el = port.find("./state")
        state = state_el.attrib.get("state","") if state_el is not None else ""
        svc = port.find("./service")
        name = (svc.attrib.get("name","") if svc is not None else "")
        ver = (svc.attrib.get("version","") if svc is not None else "")
        rows.append([addr, proto, p, state, name, ver])
w = csv.writer(sys.stdout)
w.writerow(["ip","proto","port","state","service","version"])
w.writerows(rows)
