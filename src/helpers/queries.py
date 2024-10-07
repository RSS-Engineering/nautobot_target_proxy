OOB_TARGET_QUERY = """
{
  interfaces(mgmt_only: true, name: ["iDRAC", "iLO"]) {
    device {
      name
      rack {
        name
      }
      id
      tenant {
        id
      }
      cf_core_number
      location {
        name
        parent {
          name
        }
      }
    }
    ip_addresses {
      host
    }
  }
}
"""
