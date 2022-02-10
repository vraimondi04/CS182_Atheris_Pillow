# Copyright 2022 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Example for using libprotobuf_mutator with Atheris."""

import atheris
import sys

# copybara:strip_begin
# Use google3 imports internally.
from google3.google.protobuf import wrappers_pb2
from atheris.contrib.libprotobuf_mutator import atheris_libprotobuf_mutator
# copybara:strip_end_and_replace_begin
#import atheris_libprotobuf_mutator
#from google.protobuf import wrappers_pb2
# copybara:replace_end


@atheris.instrument_func
def TestOneProtoInput(msg):
  if msg.value == 13371337:
    raise RuntimeError('Solved!')


if __name__ == '__main__':
  atheris_libprotobuf_mutator.Setup(
      sys.argv, TestOneProtoInput, proto=wrappers_pb2.Int64Value)
  atheris.Fuzz()
