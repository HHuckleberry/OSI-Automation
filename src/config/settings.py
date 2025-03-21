TIMEOUT = 10  # seconds
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
GOOGLE_SEARCH_URL = "https://www.googleapis.com/customsearch/v1"
DNS_DUMPSTER_URL = "https://dnsdumpster.com/"
SENSITIVE_KEYWORDS = [
    "SCADA", "HMI", "OT", "ICS", "sensitive data", "confidential", "credentials",
    "Allen-Bradley", "Rockwell", "PanelView Plus", "Siemens", "Schneider Electric",
    "Honeywell", "Emerson", "ABB", "GE", "Yokogawa", "Mitsubishi Electric",
    "Fanuc", "Omron", "Beckhoff", "Wago", "Phoenix Contact", "ProSoft",
    "Wonderware", "InduSoft", "FactoryTalk", "Citect", "Modicon", "DeltaV",
    "Triconex", "ControlLogix", "CompactLogix", "MicroLogix", "S7-1200", "S7-1500",
    "DCS", "PLC", "RTU", "PanelView", "VFD", "HMI Panel", "industrial automation",
    "ICS cybersecurity", "industrial control systems", "Allen Bradley",
    "process control", "supervisory control", "distributed control system",
    "industrial IoT", "IIoT", "industrial network", "fieldbus", "Profibus",
    "Profinet", "EtherNet/IP", "Modbus", "BACnet", "OPC", "industrial protocol",
    "automation system", "safety system", "control system", "engineering workstation",
    "human-machine interface", "remote terminal unit", "industrial gateway",
    "industrial firewall", "industrial router", "industrial switch", "industrial VPN",
    "ICS vulnerabilities", "ICS exploits", "ICS devices", "ICS networks", "RDP", "VNC", "Remote Desktop", "login", "logon", "pass",
    "WTP", "WWTP", "Pump Station", ""
    
]