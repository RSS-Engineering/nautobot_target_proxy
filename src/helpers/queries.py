OOB_TARGET_QUERY = """
    {
      interfaces(mgmt_only: true, name: ["iDRAC", "iLO"]) {
        device {
          name
          cf_core_number
          location {
            name
          }
        }
        ip_addresses {
          host
        }
      }
    }
"""
