# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class IptuItem(scrapy.Item):
	NomeProprietario = scrapy.Field()
	Setor = scrapy.Field()
	Quadra = scrapy.Field()
	Lote = scrapy.Field()
	Situacao = scrapy.Field()
	DigitoSQL = scrapy.Field()
	Condominio = scrapy.Field()
	NomeLogradouro = scrapy.Field()
	NrPorta = scrapy.Field()
	TipoUso = scrapy.Field()
	AreaTerreno = scrapy.Field()
	AreaConstruida = scrapy.Field()