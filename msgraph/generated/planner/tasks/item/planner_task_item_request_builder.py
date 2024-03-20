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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.planner_task import PlannerTask
    from .assigned_to_task_board_format.assigned_to_task_board_format_request_builder import AssignedToTaskBoardFormatRequestBuilder
    from .bucket_task_board_format.bucket_task_board_format_request_builder import BucketTaskBoardFormatRequestBuilder
    from .details.details_request_builder import DetailsRequestBuilder
    from .progress_task_board_format.progress_task_board_format_request_builder import ProgressTaskBoardFormatRequestBuilder

class PlannerTaskItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the tasks property of the microsoft.graph.planner entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PlannerTaskItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/planner/tasks/{plannerTask%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[PlannerTaskItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a plannerTask object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/plannertask-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[PlannerTaskItemRequestBuilderGetRequestConfiguration] = None) -> Optional[PlannerTask]:
        """
        Retrieve the properties and relationships of plannerTask object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PlannerTask]
        Find more info here: https://learn.microsoft.com/graph/api/plannertask-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.planner_task import PlannerTask

        return await self.request_adapter.send_async(request_info, PlannerTask, error_mapping)
    
    async def patch(self,body: Optional[PlannerTask] = None, request_configuration: Optional[PlannerTaskItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[PlannerTask]:
        """
        Update the navigation property tasks in planner
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PlannerTask]
        Find more info here: https://learn.microsoft.com/graph/api/plannertask-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.planner_task import PlannerTask

        return await self.request_adapter.send_async(request_info, PlannerTask, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[PlannerTaskItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a plannerTask object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/planner/tasks/{plannerTask%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[PlannerTaskItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of plannerTask object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[PlannerTask] = None, request_configuration: Optional[PlannerTaskItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property tasks in planner
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/planner/tasks/{plannerTask%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> PlannerTaskItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlannerTaskItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PlannerTaskItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assigned_to_task_board_format(self) -> AssignedToTaskBoardFormatRequestBuilder:
        """
        Provides operations to manage the assignedToTaskBoardFormat property of the microsoft.graph.plannerTask entity.
        """
        from .assigned_to_task_board_format.assigned_to_task_board_format_request_builder import AssignedToTaskBoardFormatRequestBuilder

        return AssignedToTaskBoardFormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bucket_task_board_format(self) -> BucketTaskBoardFormatRequestBuilder:
        """
        Provides operations to manage the bucketTaskBoardFormat property of the microsoft.graph.plannerTask entity.
        """
        from .bucket_task_board_format.bucket_task_board_format_request_builder import BucketTaskBoardFormatRequestBuilder

        return BucketTaskBoardFormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def details(self) -> DetailsRequestBuilder:
        """
        Provides operations to manage the details property of the microsoft.graph.plannerTask entity.
        """
        from .details.details_request_builder import DetailsRequestBuilder

        return DetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def progress_task_board_format(self) -> ProgressTaskBoardFormatRequestBuilder:
        """
        Provides operations to manage the progressTaskBoardFormat property of the microsoft.graph.plannerTask entity.
        """
        from .progress_task_board_format.progress_task_board_format_request_builder import ProgressTaskBoardFormatRequestBuilder

        return ProgressTaskBoardFormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PlannerTaskItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class PlannerTaskItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of plannerTask object.
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
    class PlannerTaskItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[PlannerTaskItemRequestBuilder.PlannerTaskItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PlannerTaskItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

