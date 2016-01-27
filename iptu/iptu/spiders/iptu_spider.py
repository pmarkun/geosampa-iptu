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
        if not self.state.has_key('lote'):
            self.state['setor'] = 0
            self.state['quadra'] = 0
            self.state['lote'] = 0
    
        print "Starting in..." + ",".join([str(self.state['setor']).zfill(3),str(self.state['quadra']).zfill(4),str(self.state['lote']).zfill(4)])
        
        for setor in range(self.state['setor'],311):
            for quadra in range(self.state['quadra'],100):
                for lote in range(self.state['lote'],100):
                    payload = { 'pCdSetor': str(setor).zfill(3), 'pCdQuadra': str(quadra).zfill(4), 'pCdLote': str(lote).zfill(4) }
                    self.state['setor'] = setor
                    self.state['quadra'] = quadra
                    self.state['lote'] = lote
                    yield Request(url, self.parse_data, method="POST", body=str(payload), headers={"Content-Type":"application/json"})
                self.state['lote'] = 0
            self.state['quadra'] = 0

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