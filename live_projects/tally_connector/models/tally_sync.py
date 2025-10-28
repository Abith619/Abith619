from odoo import models, fields
import requests

class TallySync(models.Model):
    _name = "tally.sync"
    _description = "Tally Sync Utility"

    name = fields.Char("Name")
    last_response = fields.Text("Last Tally Response")

    def send_to_tally(self, xml_payload):
        config = self.env["tally.config"].search([], limit=1)
        if not config:
            raise ValueError("Tally configuration not found")

        url = f"{config.host}:{config.port}"
        headers = {"Content-Type": "application/xml"}

        try:
            response = requests.post(url, data=xml_payload.encode("utf-8"), headers=headers)
            self.last_response = response.text
            return response.text
        except Exception as e:
            self.last_response = str(e)
            return str(e)

    def test_connection(self):
        xml_payload = """
        <ENVELOPE>
          <HEADER>
              <VERSION>1</VERSION>
              <TALLYREQUEST>Export Data</TALLYREQUEST>
              <TYPE>Collection</TYPE>
              <ID>Ledger Collection</ID>
          </HEADER>
          <BODY>
              <DESC>
                  <STATICVARIABLES>
                      <SVCURRENTCOMPANY>BWS</SVCURRENTCOMPANY>
                  </STATICVARIABLES>
                  <TDL>
                      <TDLMESSAGE>
                          <COLLECTION NAME="Ledger Collection">
                              <TYPE>Ledger</TYPE>
                              <FETCH>Name,Parent</FETCH>
                          </COLLECTION>
                      </TDLMESSAGE>
                  </TDL>
              </DESC>
          </BODY>
        </ENVELOPE>
        """
        return self.send_to_tally(xml_payload)


class ResPartner(models.Model):
    _inherit = "res.partner"

    tally_synced = fields.Boolean("Synced with Tally", default=False)

    def export_to_tally(self):
        """Export partner as Ledger in Tally"""
        sync_util = self.env["tally.sync"].create({"name": f"Export {self.name}"})

        for partner in self:
            ledger_xml = f"""
            <ENVELOPE>
              <HEADER>
                <TALLYREQUEST>Import Data</TALLYREQUEST>
              </HEADER>
              <BODY>
                <IMPORTDATA>
                  <REQUESTDESC>
                    <REPORTNAME>All Masters</REPORTNAME>
                  </REQUESTDESC>
                  <REQUESTDATA>
                    <TALLYMESSAGE xmlns:UDF="TallyUDF">
                      <LEDGER NAME="{partner.name}" ACTION="Create">
                        <NAME>{partner.name}</NAME>
                        <PARENT>{"Sundry Debtors" if partner.customer_rank > 0 else "Sundry Creditors"}</PARENT>
                        <ISBILLWISEON>Yes</ISBILLWISEON>
                        <EMAIL>{partner.email or ""}</EMAIL>
                        <ADDRESS.LIST TYPE="String">
                          <ADDRESS>{partner.street or ""}</ADDRESS>
                          <ADDRESS>{partner.city or ""}</ADDRESS>
                        </ADDRESS.LIST>
                        <PINCODE>{partner.zip or ""}</PINCODE>
                        <COUNTRYNAME>{partner.country_id.name or ""}</COUNTRYNAME>
                        <STATENAME>{partner.state_id.name or ""}</STATENAME>
                        <PHONENUMBER>{partner.phone or ""}</PHONENUMBER>
                      </LEDGER>
                    </TALLYMESSAGE>
                  </REQUESTDATA>
                </IMPORTDATA>
              </BODY>
            </ENVELOPE>
            """

            response = sync_util.send_to_tally(ledger_xml)

            if "CREATED" in response or "ALTERED" in response:
                partner.tally_synced = True

        return True
