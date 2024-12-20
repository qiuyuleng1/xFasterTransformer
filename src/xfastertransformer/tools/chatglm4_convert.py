# Copyright (c) 2024 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

from .chatglm2_convert import ChatGLM2Convert

class ChatGLM4Convert(ChatGLM2Convert):
    """
    Convert huggingface GLM4 model. Use https://huggingface.co/THUDM/glm-4-9b-chat
    """

    def __init__(self):
        super().__init__()
        self.model_type = "chatglm4"
