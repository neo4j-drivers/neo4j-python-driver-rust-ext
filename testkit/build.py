# Copyright (c) "Neo4j"
# Neo4j Sweden AB [https://neo4j.com]
#
# This file is part of Neo4j.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import shutil
from pathlib import Path
import os

from _common import (
    # DRIVER_REF,
    # DRIVER_REPO,
    run,
    # run_output,
    run_python,
)


if __name__ == "__main__":
    # run(["git", "status", "--porcelain"])
    run_python(["-m", "pip", "install", "-U", "pip"],
               warning_as_error=False)
    run_python(["-m", "pip", "install", "-Ur", "requirements-dev.txt"],
               warning_as_error=False)
    # run([
    #     "git", "clone", "--single-branch", "--branch", DRIVER_REF,
    #     "--depth", "1", f"https://github.com/neo4j/{DRIVER_REPO}",
    #     "driver_tmp",
    # ])
    # try:
    #     os.remove("tests/v1/packstream.py")
    # except FileNotFoundError:
    #     pass
    # os.rename(
    #     "driver_tmp/tests/unit/common/codec/packstream/v1/test_packstream.py",
    #     "tests/v1/packstream.py"
    # )
    # try:
    #     shutil.rmtree("testkitbackend")
    # except FileNotFoundError:
    #     pass
    # os.rename("driver_tmp/testkitbackend", "testkitbackend")
    # shutil.rmtree("driver_tmp")
