#!/usr/bin/env python3

#   Copyright 2014-2018 PUNCH Cyber Analytics Group
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os
import logging
import unittest

from stoq import RequestMeta, Stoq, Payload
from stoq.data_classes import WorkerResponse


class TestCore(unittest.TestCase):
    def setUp(self) -> None:
        self.plugin_name = 'hash_ssdeep'
        self.plugin_dir = os.path.join(os.getcwd(), self.plugin_name)
        self.generic_data = b'This is a payload to hash'
        logging.disable(logging.CRITICAL)

    def tearDown(self) -> None:
        logging.disable(logging.NOTSET)

    def test_scan(self) -> None:
        s = Stoq(plugin_dir_list=[self.plugin_dir])
        plugin = s.load_plugin(self.plugin_name)
        request_meta = RequestMeta(archive_payloads=False)
        payload = Payload(self.generic_data)
        response = plugin.scan(payload, request_meta)
        self.assertIsInstance(response, WorkerResponse)
        self.assertEqual('3:hMCE7pr3Kn:huJ6', response.results['ssdeep'])