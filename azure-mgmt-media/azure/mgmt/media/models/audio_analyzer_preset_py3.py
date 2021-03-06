# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .preset import Preset


class AudioAnalyzerPreset(Preset):
    """The Audio Analyzer preset applies a pre-defined set of AI-based analysis
    operations, including speech transcription. Currently, the preset supports
    processing of content with a single audio track.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: VideoAnalyzerPreset

    All required parameters must be populated in order to send to Azure.

    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param audio_language: The language for the audio payload in the input
     using the BCP-47 format of 'language tag-region' (e.g: 'en-US'). The list
     of supported languages are, 'en-US', 'en-GB', 'es-ES', 'es-MX', 'fr-FR',
     'it-IT', 'ja-JP', 'pt-BR', 'zh-CN'.
    :type audio_language: str
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'audio_language': {'key': 'audioLanguage', 'type': 'str'},
    }

    _subtype_map = {
        'odatatype': {'#Microsoft.Media.VideoAnalyzerPreset': 'VideoAnalyzerPreset'}
    }

    def __init__(self, *, audio_language: str=None, **kwargs) -> None:
        super(AudioAnalyzerPreset, self).__init__(**kwargs)
        self.audio_language = audio_language
        self.odatatype = '#Microsoft.Media.AudioAnalyzerPreset'
