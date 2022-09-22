#!/usr/bin/env python3

# Copyright 2022 Peter Hoffmann <Hoffmann.P@gmx.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',0))
s.sendto(b'\x30\x67\x30\x66', ('192.168.4.153', 8070))
s.sendto(b'\x42\x76', ('192.168.4.153', 8080))
while True:
    (buf, rinfo) = s.recvfrom(4096)
    port = rinfo[1]
    if port == 8080:
        sys.stdout.buffer.write(buf[8:])
    else:
        sys.stderr.buffer.write(bytes(port))
