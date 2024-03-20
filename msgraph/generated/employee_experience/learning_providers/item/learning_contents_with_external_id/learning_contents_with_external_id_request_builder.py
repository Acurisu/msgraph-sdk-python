from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.learning_content import LearningContent
    from .....models.o_data_errors.o_data_error import ODataError

class LearningContentsWithExternalIdRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the learningContents property of the microsoft.graph.learningProvider entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]], external_id: Optional[str] = None) -> None:
        """
        Instantiates a new LearningContentsWithExternalIdRequestBuilder and sets the default values.
        param external_id: Alternate key of learningContent
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['externalId'] = str(external_id)
        super().__init__(request_adapter, "{+baseurl}/employeeExperience/learningProviders/{learningProvider%2Did}/learningContents(externalId='{externalId}'){?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[LearningContentsWithExternalIdRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete the specified learningContent resource that represents the metadata of the specified provider's ingested content.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/learningprovider-delete-learningcontents?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[LearningContentsWithExternalIdRequestBuilderGetRequestConfiguration] = None) -> Optional[LearningContent]:
        """
        Get the specified learningContent resource which represents the metadata of the specified provider's ingested content.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LearningContent]
        Find more info here: https://learn.microsoft.com/graph/api/learningcontent-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.learning_content import LearningContent

        return await self.request_adapter.send_async(request_info, LearningContent, error_mapping)
    
    async def patch(self,body: Optional[LearningContent] = None, request_configuration: Optional[LearningContentsWithExternalIdRequestBuilderPatchRequestConfiguration] = None) -> Optional[LearningContent]:
        """
        Update the navigation property learningContents in employeeExperience
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LearningContent]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.learning_content import LearningContent

        return await self.request_adapter.send_async(request_info, LearningContent, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[LearningContentsWithExternalIdRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete the specified learningContent resource that represents the metadata of the specified provider's ingested content.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/employeeExperience/learningProviders/{learningProvider%2Did}/learningContents(externalId='{externalId}')', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[LearningContentsWithExternalIdRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the specified learningContent resource which represents the metadata of the specified provider's ingested content.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[LearningContent] = None, request_configuration: Optional[LearningContentsWithExternalIdRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property learningContents in employeeExperience
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/employeeExperience/learningProviders/{learningProvider%2Did}/learningContents(externalId='{externalId}')', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> LearningContentsWithExternalIdRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LearningContentsWithExternalIdRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return LearningContentsWithExternalIdRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class LearningContentsWithExternalIdRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class LearningContentsWithExternalIdRequestBuilderGetQueryParameters():
        """
        Get the specified learningContent resource which represents the metadata of the specified provider's ingested content.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class LearningContentsWithExternalIdRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[LearningContentsWithExternalIdRequestBuilder.LearningContentsWithExternalIdRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class LearningContentsWithExternalIdRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

