#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# created by: zhangzhongyu

BOT_NAME = 'crawl2mongo'

SPIDER_MODULES = ['crawl2mongo.spiders']
NEWSPIDER_MODULE = 'crawl2mongo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'

DOWNLOAD_DELAY = 2

PATH_DEBUG = True
PATH_DEBUG_URL_LENGTH = 97

ITEM_PIPELINES = ['crawl2mongo.pipelines.mongodbPipeline']

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "truonex"
MONGODB_COLLECTION = "projects"

# Maximum number of concurrent items (per response) to process in parallel in the Item Processor (also known as the Item Pipeline).
CONCURRENT_ITEMS = 100

# The maximum number of concurrent (ie. simultaneous) requests that will be performed by the Scrapy downloader.
# The maximum number of requests that the request_container can fill-up.  The container is filled to capacity with the requests.  Then as one exits, another fills its spot.  When there are no more requests to fill a vacancy, the container simply empties.
# This effect is most noticibly when 'Closing spider (shutdown)'
CONCURRENT_REQUESTS = 8

# The maximum number of concurrent (ie. simultaneous) requests that will be performed to any single domain.
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# The maximum number of concurrent (ie. simultaneous) requests that will be performed to any single IP. If non-zero, the CONCURRENT_REQUESTS_PER_DOMAIN setting is ignored, and this one is used instead. In other words, concurrency limits will be applied per IP, not per domain
CONCURRENT_REQUESTS_PER_IP = 0

DOWNLOADER_STATS = True
RANDOMIZE_DOWNLOAD_DELAY = True
