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

try:
    from .train_request_py3 import TrainRequest
    from .form_document_report_py3 import FormDocumentReport
    from .form_operation_error_py3 import FormOperationError
    from .train_result_py3 import TrainResult
    from .keys_result_py3 import KeysResult
    from .model_result_py3 import ModelResult
    from .models_result_py3 import ModelsResult
    from .inner_error_py3 import InnerError
    from .error_information_py3 import ErrorInformation
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .extracted_token_py3 import ExtractedToken
    from .extracted_key_value_pair_py3 import ExtractedKeyValuePair
    from .extracted_table_column_py3 import ExtractedTableColumn
    from .extracted_table_py3 import ExtractedTable
    from .extracted_page_py3 import ExtractedPage
    from .analyze_result_py3 import AnalyzeResult
except (SyntaxError, ImportError):
    from .train_request import TrainRequest
    from .form_document_report import FormDocumentReport
    from .form_operation_error import FormOperationError
    from .train_result import TrainResult
    from .keys_result import KeysResult
    from .model_result import ModelResult
    from .models_result import ModelsResult
    from .inner_error import InnerError
    from .error_information import ErrorInformation
    from .error_response import ErrorResponse, ErrorResponseException
    from .extracted_token import ExtractedToken
    from .extracted_key_value_pair import ExtractedKeyValuePair
    from .extracted_table_column import ExtractedTableColumn
    from .extracted_table import ExtractedTable
    from .extracted_page import ExtractedPage
    from .analyze_result import AnalyzeResult

__all__ = [
    'TrainRequest',
    'FormDocumentReport',
    'FormOperationError',
    'TrainResult',
    'KeysResult',
    'ModelResult',
    'ModelsResult',
    'InnerError',
    'ErrorInformation',
    'ErrorResponse', 'ErrorResponseException',
    'ExtractedToken',
    'ExtractedKeyValuePair',
    'ExtractedTableColumn',
    'ExtractedTable',
    'ExtractedPage',
    'AnalyzeResult',
]