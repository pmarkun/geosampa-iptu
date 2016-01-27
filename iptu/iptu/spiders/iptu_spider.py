import scrapy
from scrapy import Request
import urllib
import json
from iptu.items import IptuItem

url = "http://geosampa.prefeitura.sp.gov.br/PaginasPublicas/_SBC.aspx/pesquisaLoteIntegracaoTPCL"

class IptuSpider(scrapy.Spider):
    name = "iptu"
    allowed_domains = ["geosampa.prefeitura.sp.gov.br"]
    
    
    def start_requests(self):
        payload = { 'pCdSetor': '114', 'pCdQuadra': '249', 'pCdLote': '0090' }
        yield Request(url, self.parse_data, method="POST", body=str(payload), headers={"Content-Type":"application/json"})

    def parse_data(self, response):
        # do stuff with data...
        data_raw = json.loads(response.body)
        for data in data_raw['d']:
            item = IptuItem()
            item['NomeProprietario'] = data['NomeProprietario']
            item['Setor'] = data['Setor']
            item['Quadra'] = data['Quadra']
            item['Lote'] = data['Lote']
            item['Situacao'] = data['Situacao']
            item['DigitoSQL'] = data['DigitoSQL']
            item['Condominio'] = data['Condominio']
            item['NomeLogradouro'] = data['NomeLogradouro']
            item['NrPorta'] = data['NrPorta']
            item['TipoUso'] = data['TipoUso']
            item['AreaTerreno'] = data['AreaTerreno']
            item['AreaConstruida'] = data['AreaConstruida']
            yield item